# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoplayer_uigwLuhD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Videoplayer(object):
    def setupUi(self, Videoplayer):
        if not Videoplayer.objectName():
            Videoplayer.setObjectName(u"Videoplayer")
        Videoplayer.resize(800, 600)
        self.actionOpen = QAction(Videoplayer)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(Videoplayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border:none")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_window = QFrame(self.centralwidget)
        self.frame_window.setObjectName(u"frame_window")
        self.frame_window.setStyleSheet(u"border: none")
        self.frame_window.setFrameShape(QFrame.StyledPanel)
        self.frame_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_window)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 30))
        self.frame_top.setStyleSheet(u"background-color: rgb(0,0,0);\n"
"border: none;")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.frame_top)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(30, 30))
        self.frame_logo.setMaximumSize(QSize(40, 16777215))
        self.frame_logo.setStyleSheet(u"image: url(:/16x16/icons/16x16/cil-movie.png);\n"
"background-color: rgb(85, 0, 2);")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_logo)

        self.frame_appName = QFrame(self.frame_top)
        self.frame_appName.setObjectName(u"frame_appName")
        self.frame_appName.setMinimumSize(QSize(0, 30))
        self.frame_appName.setFrameShape(QFrame.StyledPanel)
        self.frame_appName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_appName)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_appName = QLabel(self.frame_appName)
        self.label_appName.setObjectName(u"label_appName")
        self.label_appName.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"HP Simplified")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_appName.setFont(font)
        self.label_appName.setStyleSheet(u"color: rgb(130,0,0);")

        self.horizontalLayout_2.addWidget(self.label_appName)


        self.horizontalLayout.addWidget(self.frame_appName)

        self.frame_btns_right = QFrame(self.frame_top)
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
"	background-color: rgb(255, 14, 6);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_window)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(0, 460))
        self.frame_center.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.frame_center.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame_center)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.openGLWidget = QOpenGLWidget(self.frame_center)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout_2.addWidget(self.openGLWidget, 0, 0, 1, 1)

        self.frame_controls = QFrame(self.frame_center)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setMaximumSize(QSize(16777215, 100))
        self.frame_controls.setLayoutDirection(Qt.LeftToRight)
        self.frame_controls.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_controls)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progress_videotime = QProgressBar(self.frame_controls)
        self.progress_videotime.setObjectName(u"progress_videotime")
        self.progress_videotime.setMinimumSize(QSize(579, 8))
        self.progress_videotime.setMaximumSize(QSize(16777215, 8))
        self.progress_videotime.setValue(24)

        self.gridLayout_3.addWidget(self.progress_videotime, 0, 0, 1, 3)

        self.frame_7 = QFrame(self.frame_controls)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(332, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_7, 1, 0, 1, 1)

        self.frame_playpause = QFrame(self.frame_controls)
        self.frame_playpause.setObjectName(u"frame_playpause")
        self.frame_playpause.setMinimumSize(QSize(132, 90))
        self.frame_playpause.setMaximumSize(QSize(132, 90))
        self.frame_playpause.setMouseTracking(False)
        self.frame_playpause.setStyleSheet(u"background-color: rgb(249, 249, 249);")
        self.frame_playpause.setFrameShape(QFrame.StyledPanel)
        self.frame_playpause.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_playpause)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, -1, -1, 0)
        self.btn_previous = QPushButton(self.frame_playpause)
        self.btn_previous.setObjectName(u"btn_previous")
        self.btn_previous.setMinimumSize(QSize(35, 35))
        self.btn_previous.setMaximumSize(QSize(35, 35))
        self.btn_previous.setStyleSheet(u"QPushButton{\n"
"image: url(:/16x16/icons/16x16/cil-media-step-backward.png);\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"		background-color: rgb(85, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_previous.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_previous, 0, 0, 1, 1)

        self.btn_play = QPushButton(self.frame_playpause)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(35, 35))
        self.btn_play.setMaximumSize(QSize(35, 35))
        self.btn_play.setStyleSheet(u"QPushButton{\n"
"image: url(:/16x16/icons/16x16/cil-media-play.png);\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_play.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_play, 0, 1, 1, 1)

        self.btn_next = QPushButton(self.frame_playpause)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(35, 35))
        self.btn_next.setMaximumSize(QSize(35, 35))
        self.btn_next.setStyleSheet(u"QPushButton{\n"
"image: url(:/16x16/icons/16x16/cil-media-step-forward.png);\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_next.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_next, 0, 2, 1, 1)

        self.btn_stop = QPushButton(self.frame_playpause)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(35, 35))
        self.btn_stop.setMaximumSize(QSize(35, 35))
        self.btn_stop.setStyleSheet(u"QPushButton{\n"
"image: url(:/16x16/icons/16x16/cil-media-stop.png);\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(132, 132, 132);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_stop.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_stop, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_playpause, 1, 1, 1, 1)

        self.frame_volume = QFrame(self.frame_controls)
        self.frame_volume.setObjectName(u"frame_volume")
        self.frame_volume.setLayoutDirection(Qt.LeftToRight)
        self.frame_volume.setFrameShape(QFrame.StyledPanel)
        self.frame_volume.setFrameShadow(QFrame.Raised)
        self.slider_volume = QSlider(self.frame_volume)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setGeometry(QRect(170, 40, 160, 8))
        self.slider_volume.setMinimumSize(QSize(160, 0))
        self.slider_volume.setMaximumSize(QSize(160, 8))
        self.slider_volume.setStyleSheet(u"QSlider:pressed {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.46, x2:1, y2:0.414773, stop:0.113636 rgba(253, 238, 34, 255), stop:0.795455 rgba(254, 27, 11, 255));\n"
"}\n"
"")
        self.slider_volume.setOrientation(Qt.Horizontal)
        self.label_volume = QLabel(self.frame_volume)
        self.label_volume.setObjectName(u"label_volume")
        self.label_volume.setGeometry(QRect(6, 30, 161, 20))
        font1 = QFont()
        font1.setFamily(u"MS Serif")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_volume.setFont(font1)
        self.label_volume.setLayoutDirection(Qt.RightToLeft)
        self.label_volume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.frame_volume, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_controls, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_center)


        self.gridLayout.addWidget(self.frame_window, 0, 0, 1, 1)

        Videoplayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Videoplayer)

        QMetaObject.connectSlotsByName(Videoplayer)
    # setupUi

    def retranslateUi(self, Videoplayer):
        Videoplayer.setWindowTitle(QCoreApplication.translate("Videoplayer", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("Videoplayer", u"Open", None))
        self.label_appName.setText(QCoreApplication.translate("Videoplayer", u"  Movie_App", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Videoplayer", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("Videoplayer", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Videoplayer", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.btn_previous.setText("")
        self.btn_play.setText("")
        self.btn_next.setText("")
        self.btn_stop.setText("")
        self.label_volume.setText(QCoreApplication.translate("Videoplayer", u"Volume", None))
    # retranslateUi

