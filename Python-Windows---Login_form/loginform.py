################################################################################
#
# @Author: Mark_T
# @Title: Login Form Template
# @Credit: Qt Designer (Came with Pyside2)
# @version: 1.0
#
################################################################################

#Import needed libraries
import sys, platform
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt,QEvent


# import Loginform UI code
from ui_loginform import Ui_Loginform
from Ui_functions import *

GLOBAL_STATE = 0

#Loginform Class definition for unique Loginforms
class Loginform(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loginform()
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
 
        # widget to be moved
        self.ui.frame_9.mousePressEvent = self.mousePressEvent
        self.ui.frame_9.mouseMoveEvent = self.moveWindow


    ################################################################################

        # Display Window
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

   #Move the window
    def moveWindow(self,event):
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
    window = Loginform()
    sys.exit(app.exec_())