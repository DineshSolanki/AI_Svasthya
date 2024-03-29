import os

import cv2
import dlib
import imutils
from imutils import face_utils
from imutils.video import VideoStream
from plyer import notification
from scipy.spatial import distance as dist

import Util
from InfiniteTimer import InfiniteTimer
from Util import get_timeout
from telegrambot import notify_bot


def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])
    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    # return the eye aspect ratio
    return ear


# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold
EYE_AR_THRESH = 0.23
EYE_AR_CONSEC_FRAMES = 2
# initialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)


# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True,
#                 help="path to facial landmark predictor")
# ap.add_argument("-v", "--video", type=str, default="",
#                 help="path to input video file")
# args = vars(ap.parse_args())

def start_blink_detection():
    filename = r"data/shape_predictor_68_face_landmarks.dat"
    url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"

    if not os.path.exists(filename):
        print(f"{filename} not found, downloading...")
        Util.download_file(url, filename + ".bz2")
        Util.decompress_file(filename)

    if not Util.check_camera_availability():
        return

    global COUNTER
    global TOTAL
    rest_timer = InfiniteTimer(float(30), send_rest_notification)
    rest_timer.start()
    blink_timer = InfiniteTimer(float(get_timeout()) * 60, send_blink_notification, "Blink!! {}".format(TOTAL))
    blink_timer.start()
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()

    predictor = dlib.shape_predictor(filename)
    # grab the indexes of the facial landmarks for the left and
    # right eye, respectively
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    # start the video stream thread
    print("[INFO] starting video stream thread...")
    # vs = FileVideoStream(args["video"]).start()
    # fileStream = True
    vs = VideoStream(src=0).start()
    # vs = VideoStream(usePiCamera=True).start()
    fileStream = False
    # loop over frames from the video stream
    while True:
        # if this is a file video stream, then we need to check if
        # there any more frames left in the buffer to process
        if fileStream and not vs.more():
            break
        # grab the frame from the threaded video file stream, resize
        # it, and convert it to grayscale
        # channels)
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detect faces in the grayscale frame
        rects = detector(gray, 0)

        # loop over the face detections
        for rect in rects:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            if rest_timer.is_running:
                rest_timer.cancel()
            rest_timer.start()
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            # extract the left and right eye coordinates, then use the
            # coordinates to compute the eye aspect ratio for both eyes
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            # average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            # compute the convex hull for the left and right eye, then
            # visualize each of the eyes
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # check to see if the eye aspect ratio is below the blink
            # threshold, and if so, increment the blink frame counter
            if ear < EYE_AR_THRESH:
                COUNTER += 1
            # otherwise, the eye aspect ratio is not below the blink
            # threshold
            else:
                # if the eyes were closed for a sufficient number of
                # then increment the total number of blinks
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    TOTAL += 1
                    if blink_timer.is_running:
                        blink_timer.cancel()
                    blink_timer.start()

                # reset the eye frame counter
                COUNTER = 0

                # draw the total number of blinks on the frame along with
                # the computed eye aspect ratio for the frame
                cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # show the frame
        cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("AI_Svasthya", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    # do a bit of cleanup
    if rest_timer.is_running:
        rest_timer.cancel()
    if blink_timer.is_running:
        blink_timer.cancel()
    cv2.destroyAllWindows()
    vs.stop()


def send_window_notification(title, message, app_icon=None, timeout=5):
    notification.notify(
        title=title,
        message=message,
        app_icon=app_icon,  # e.g. 'C:\\icon_32x32.ico'
        timeout=timeout,  # seconds
    )


def send_rest_notification():
    if Util.get_screen_rest_monitoring():
        if Util.get_notification_enabled():
            send_window_notification('Screen Rest', "It's been 20 minutes since you took screen rest.",
                                     "Assets/coffee.ico",timeout=10)
        if Util.get_smart_notification_enabled():
            notify_bot(f"Screen Rest time!!")


def send_blink_notification():
    if Util.get_blink_monitoring():
        if Util.get_notification_enabled():
            send_window_notification('Blink', f'Blink Count ={TOTAL}', "Assets/eye.ico")
        if Util.get_smart_notification_enabled():
            notify_bot(f"Blink!!\n Blink Count = {TOTAL}")
