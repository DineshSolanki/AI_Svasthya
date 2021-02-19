import threading
from datetime import timedelta


def hello():
    print("hello, world")


duration = timedelta(hours=0, minutes=1).total_seconds()
t = threading.Timer(duration, hello)
t.start()
