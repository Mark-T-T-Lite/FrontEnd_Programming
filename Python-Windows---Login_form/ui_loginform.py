# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginform_uiRZVBQn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Loginform(object):
    def setupUi(self, Loginform):
        if not Loginform.objectName():
            Loginform.setObjectName(u"Loginform")
        Loginform.resize(800, 700)
        self.centralwidget = QWidget(Loginform)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#frame{\n"
"	background-color: rgb(0, 0, 0);\n"
"	image: url(:/16x16/C:/Users/Public/Pictures/Sample Pictures/Koala.jpg);\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background: opaque")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(40, 30))
        self.frame_10.setMaximumSize(QSize(40, 30))
        self.frame_10.setStyleSheet(u"image: url(:/16x16/icons/16x16/cil-user-female.png);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"Narkisim")
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(56, 222, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_btns_right = QFrame(self.frame_3)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setLayoutDirection(Qt.LeftToRight)
        self.frame_btns_right.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_2.addWidget(self.frame_btns_right)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 510))
        self.frame_2.setMaximumSize(QSize(400, 510))
        self.frame_2.setStyleSheet(u"background-color: rgb(5, 5, 5);\n"
"border-radius:10")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 9, 381, 71))
        font2 = QFont()
        font2.setFamily(u"Viner Hand ITC")
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(19, 251, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 101, 31))
        font3 = QFont()
        font3.setFamily(u"Garamond")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(37, 255, 190);")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 253, 101, 21))
        font4 = QFont()
        font4.setFamily(u"Garamond")
        font4.setPointSize(12)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(34, 255, 240);")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 160, 341, 41))
        font5 = QFont()
        font5.setFamily(u"Garamond")
        font5.setPointSize(11)
        self.textEdit.setFont(font5)
        self.textEdit.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.textEdit.setInputMethodHints(Qt.ImhNone)
        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(30, 280, 341, 41))
        self.textEdit_2.setFont(font5)
        self.textEdit_2.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.textEdit_2.setInputMethodHints(Qt.ImhNone)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 370, 75, 23))
        font6 = QFont()
        font6.setFamily(u"Narkisim")
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        self.pushButton.setFont(font6)
        self.pushButton.setStyleSheet(u"background-color: rgb(35, 255, 218);")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(16, 452, 371, 51))
        font7 = QFont()
        font7.setFamily(u"Times New Roman")
        font7.setPointSize(9)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"color: rgb(99, 99, 99);")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 90, 61, 16))
        font8 = QFont()
        font8.setBold(True)
        font8.setWeight(75)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 210, 321, 16))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 330, 321, 16))
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(330, 280, 40, 40))
        self.frame_8.setMinimumSize(QSize(40, 40))
        self.frame_8.setMaximumSize(QSize(40, 40))
        self.frame_8.setStyleSheet(u"\n"
"background-color: rgb(81, 81, 81);\n"
"image: url(:/16x16/icons/16x16/cil-x-circle.png);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Loginform.setCentralWidget(self.centralwidget)

        self.retranslateUi(Loginform)

        QMetaObject.connectSlotsByName(Loginform)
    # setupUi

    def retranslateUi(self, Loginform):
        Loginform.setWindowTitle(QCoreApplication.translate("Loginform", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Loginform", u"Log_In", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Loginform", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("Loginform", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Loginform", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("Loginform", u"T_Corp POS", None))
        self.label_3.setText(QCoreApplication.translate("Loginform", u"UserName", None))
        self.label_4.setText(QCoreApplication.translate("Loginform", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Loginform", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("Loginform", u"By continuing you accept the Terms of Use and Privacy Policy. You also\n"
"accept that you are aware that your data will be stored outside of Uganda and\n"
" that you are above the age of 16.", None))
        self.label_6.setText(QCoreApplication.translate("Loginform", u"v1.0", None))
        self.label_7.setText("")
        self.label_8.setText("")
    # retranslateUi

