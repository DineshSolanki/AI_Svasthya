from PyQt5.QtCore import QMetaObject, QCoreApplication, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QStatusBar, QMenuBar, QSizePolicy, QCheckBox, QHBoxLayout, QLayout, \
    QGridLayout, QWidget, QVBoxLayout, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(423, 320)
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
        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        font1.setItalic(True)
        self.checkBox_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.checkBox_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 141, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Open Sans")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 10, 141, 21))
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font2)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(180, 40, 233, 68))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_3 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font1)

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy1.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy1)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 170, 411, 101))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 130, 141, 31))
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 423, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI - Svasthya", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Screen Rest", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Eye Blinks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Show Notification Banner", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Connect to Smartphone", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Blink warning after(minutes)-", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

