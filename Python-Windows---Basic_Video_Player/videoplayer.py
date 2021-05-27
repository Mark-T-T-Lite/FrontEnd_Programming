################################################################################
#
# @Author: Mark_T
# @Title: VideoPlayer Template
# @Credit: Qt Designer (Came with Pyside2)
# @version: 1.0
#
################################################################################

#Import needed libraries
import sys, platform
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QObject, QEvent, QTimer,QPropertyAnimation,QEasingCurve
from PySide2.QtGui import QColor,QIcon

# import Videoplayer UI code
from ui_videoplayer import Ui_Videoplayer
from Ui_functions import *

GLOBAL_STATE = 0
#VideoPlayer Class definition for unique video-players
class Videoplayer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Videoplayer()
        self.ui.setupUi(self)

    ################################################################################
    #Initialize the UI.
    ################################################################################
        #Hide title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        #Onclick Listeners for Window buttons
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_maximize_restore.clicked.connect(lambda: Ui_Functions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.frame_center.mouseDoubleClickEvent = self.double_ClickMaximizeRestore
        # widget to be moved
        self.ui.frame_top.mousePressEvent = self.mousePressEvent
        self.ui.frame_top.mouseMoveEvent = self.moveWindow


    ################################################################################
    
        # Display Window
        self.show()
   
   #Maximise on double Clicking the center frame
    def double_ClickMaximizeRestore(self, event):
        print("Done")
        # IF DOUBLE CLICK CHANGE STATUS
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: Ui_Functions.maximize_restore(self))
            QTimer.singleShot(1000, lambda: Ui_Functions.hideCtrlAnimate(self))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

   #Move the window
    def moveWindow(self,event):
        print("Here")
        # If maximised, return to normal
        if GLOBAL_STATE == 1:
            Ui_Functions.maximize_restore(self)

        # moving the window
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
 


#  Where Execution starts from
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Videoplayer()
    sys.exit(app.exec_())