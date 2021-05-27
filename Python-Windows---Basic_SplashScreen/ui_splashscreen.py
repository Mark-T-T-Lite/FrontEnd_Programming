# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreenqVdFxJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(600, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.ShadowFrame = QFrame(self.centralwidget)
        self.ShadowFrame.setObjectName(u"ShadowFrame")
        self.ShadowFrame.setStyleSheet(u"QFrame \n"
"{\n"
"	color: rgb(199, 199, 199);\n"
"	background-color: rgb(9, 9, 9);\n"
"	border-radius: 10\n"
"}")
        self.ShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.ShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.ShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 80, 571, 91))
        font = QFont()
        font.setFamily(u"Gabriola")
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(7, 202, 147);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.ShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(20, 160, 571, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(12)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(159, 159, 159);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.ShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 300, 551, 16))
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"	background-color: rgb(11, 11, 11);\n"
"	color: rgb(26, 240, 158);\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"	QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0.011, y1:0.512, x2:1, y2:0.54, stop:0.181818 rgba(5, 48, 43, 255), stop:1 rgba(0, 255, 255, 255));\n"
"border-radius: 10;\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.ShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(30, 330, 581, 16))
        font2 = QFont()
        font2.setFamily(u"Calibri Light")
        font2.setPointSize(11)
        font2.setItalic(True)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(159, 159, 159);")
        self.label_loading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_version = QLabel(self.ShadowFrame)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(470, 360, 100, 16))
        font3 = QFont()
        font3.setFamily(u"Britannic Bold")
        font3.setPointSize(11)
        font3.setItalic(False)
        self.label_version.setFont(font3)
        self.label_version.setStyleSheet(u"color: rgb(159, 159, 159);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.ShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"T_Corp POS", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"T_Corp<strong> POS</strong>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"Powered by Mark_T", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"Loading Files...", None))
        self.label_version.setText(QCoreApplication.translate("SplashScreen", u"v 1.0", None))
    # retranslateUi

