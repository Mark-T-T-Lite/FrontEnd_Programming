################################################################################
#
# @Author: Mark_T
# @Title: LoginForm Template
# @Credit: Qt Designer (Came with Pyside2)
# @version: 1.0
#
################################################################################

#Import needed libraries
from loginform import *
from PySide2.QtGui import QIcon

class Ui_Functions(QMainWindow):
    ########################################################################
    # MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width(), self.height())
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))


    # def hideCtrlAnimate(self):
    #     # ANIMATION
    #     self.animation = QPropertyAnimation(self.ui.frame_controls, b"maximumHeight")
    #     self.animation.setDuration(400)
    #     self.animation.setStartValue(100)
    #     self.animation.setEndValue(10)
    #     self.animation.setEasingCurve(QEasingCurve.InOutQuart)
    #     self.animation.start()
    #     #self.ui.frame_controls.hide()
        