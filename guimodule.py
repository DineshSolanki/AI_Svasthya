from PyQt5.QtCore import QMetaObject, QCoreApplication, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QStatusBar, QMenuBar, QSizePolicy, QCheckBox, QHBoxLayout, QLayout, \
    QGridLayout, QWidget, QVBoxLayout, QLineEdit, QPushButton, QApplication

import Util
from blink_detection import start_blink_detection
from telegrambot import notify_bot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(423, 347)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 123, 68))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chkScreenRest = QCheckBox(self.gridLayoutWidget)
        self.chkScreenRest.setObjectName(u"chkScreenRest")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chkScreenRest.sizePolicy().hasHeightForWidth())
        self.chkScreenRest.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.chkScreenRest.setFont(font)
        self.chkScreenRest.setChecked(False)

        self.verticalLayout_2.addWidget(self.chkScreenRest)

        self.chkEyeBlink = QCheckBox(self.gridLayoutWidget)
        self.chkEyeBlink.setObjectName(u"chkEyeBlink")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        font1.setItalic(True)
        self.chkEyeBlink.setFont(font1)

        self.verticalLayout_2.addWidget(self.chkEyeBlink)

        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.lblMonitor = QLabel(self.centralwidget)
        self.lblMonitor.setObjectName(u"lblMonitor")
        self.lblMonitor.setGeometry(QRect(20, 10, 141, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblMonitor.sizePolicy().hasHeightForWidth())
        self.lblMonitor.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Open Sans")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.lblMonitor.setFont(font2)
        self.lblNotification = QLabel(self.centralwidget)
        self.lblNotification.setObjectName(u"lblNotification")
        self.lblNotification.setGeometry(QRect(190, 10, 141, 21))
        sizePolicy2.setHeightForWidth(self.lblNotification.sizePolicy().hasHeightForWidth())
        self.lblNotification.setSizePolicy(sizePolicy2)
        self.lblNotification.setFont(font2)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(180, 40, 233, 68))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chkNotificationBanner = QCheckBox(self.gridLayoutWidget_2)
        self.chkNotificationBanner.setObjectName(u"chkNotificationBanner")
        self.chkNotificationBanner.setFont(font1)

        self.verticalLayout.addWidget(self.chkNotificationBanner)

        self.chkConnectSmartphone = QCheckBox(self.gridLayoutWidget_2)
        self.chkConnectSmartphone.setObjectName(u"chkConnectSmartphone")
        sizePolicy1.setHeightForWidth(self.chkConnectSmartphone.sizePolicy().hasHeightForWidth())
        self.chkConnectSmartphone.setSizePolicy(sizePolicy1)
        self.chkConnectSmartphone.setFont(font)
        self.chkConnectSmartphone.setChecked(False)

        self.verticalLayout.addWidget(self.chkConnectSmartphone)

        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.lblSetting = QLabel(self.centralwidget)
        self.lblSetting.setObjectName(u"lblSetting")
        self.lblSetting.setGeometry(QRect(20, 120, 141, 31))
        sizePolicy2.setHeightForWidth(self.lblSetting.sizePolicy().hasHeightForWidth())
        self.lblSetting.setSizePolicy(sizePolicy2)
        self.lblSetting.setFont(font2)
        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(50, 270, 161, 31))
        font3 = QFont()
        font3.setFamily(u"Malgun Gothic")
        font3.setPointSize(14)
        self.btnStart.setFont(font3)
        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setGeometry(QRect(260, 270, 91, 31))
        self.btnStop.setFont(font3)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 160, 409, 99))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblBlinkTime = QLabel(self.widget)
        self.lblBlinkTime.setObjectName(u"lblBlinkTime")

        self.horizontalLayout.addWidget(self.lblBlinkTime)

        self.txtBlinkTime = QLineEdit(self.widget)
        self.txtBlinkTime.setObjectName(u"txtBlinkTime")
        font4 = QFont()
        font4.setPointSize(10)
        self.txtBlinkTime.setFont(font4)

        self.horizontalLayout.addWidget(self.txtBlinkTime)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 423, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        # settingsRestoration
        self.chkScreenRest.setChecked(Util.get_screen_rest_monitoring())
        self.chkEyeBlink.setChecked(Util.get_blink_monitoring())
        self.chkNotificationBanner.setChecked(Util.get_notification_enabled())
        self.chkConnectSmartphone.setChecked(Util.get_smart_notification())

        # events
        self.btnStart.clicked.connect(lambda: start_blink_detection())  # Set Start button
        self.chkScreenRest.stateChanged.connect(lambda: Util.set_screen_rest_monitoring(self.chkScreenRest.isChecked()))
        self.chkEyeBlink.stateChanged.connect(lambda: Util.set_blink_monitoring(self.chkEyeBlink.isChecked()))
        self.chkConnectSmartphone.stateChanged.connect(lambda: Util.set_smart_notification())
        self.chkNotificationBanner.stateChanged.connect(
            lambda: Util.set_notification_enabled(self.chkNotificationBanner.isChecked()))
        self.txtBlinkTime.editingFinished.connect(lambda: Util.set_timeout(self.txtBlinkTime.text()))

        self.btnStop.clicked.connect(QApplication.instance().quit)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI - Svasthya", None))
        self.chkScreenRest.setText(QCoreApplication.translate("MainWindow", u"Screen Rest", None))
        self.chkEyeBlink.setText(QCoreApplication.translate("MainWindow", u"Eye Blinks", None))
        self.lblMonitor.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.lblNotification.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.chkNotificationBanner.setText(QCoreApplication.translate("MainWindow", u"Show Notification Banner", None))
        self.chkConnectSmartphone.setText(QCoreApplication.translate("MainWindow", u"Connect to Smartphone", None))
        self.lblSetting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start monitoring", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop ", None))
        self.lblBlinkTime.setText(QCoreApplication.translate("MainWindow", u"Blink warning after not blinked for(per "
                                                                           u"minute)-", None))
        self.txtBlinkTime.setText(QCoreApplication.translate("MainWindow", u"15", None))
    # translateUi
