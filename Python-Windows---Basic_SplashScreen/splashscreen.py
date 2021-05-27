################################################################################
#
# @Author: Mark_T
# @Title: SplashScreen Template
# @Credit: Qt Designer (Came with Pyside2)
# @version: 1.0
#
################################################################################

import sys,platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# import SplashScreen UI code and main window
from ui_splashscreen import Ui_SplashScreen

# global variables
counter = 0

# Class for Splashscreen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # Hide title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## configure drop shadow
        self.dropShadow = QGraphicsDropShadowEffect(self)
        self.dropShadow.setXOffset(0)
        self.dropShadow.setYOffset(0)
        self.dropShadow.setBlurRadius(20)        
        self.dropShadow.setColor(QColor(0, 0, 0, 60))
        self.ui.ShadowFrame.setGraphicsEffect(self.dropShadow)

        #start a Qtimer connected to the progressbar
        self.qTimer = QtCore.QTimer()
        self.qTimer.timeout.connect(self.progress)
        self.qTimer.start(200)

        #Changes in the text as it loads    
        QtCore.QTimer.singleShot(5000, lambda: self.ui.label_loading.setText("<strong>Reading</strong> Database Files..."))
        QtCore.QTimer.singleShot(10000, lambda: self.ui.label_loading.setText("<strong>Initialisiing:</strong> User Interface..."))
        QtCore.QTimer.singleShot(14000, lambda: self.ui.label_description.setText("Custom made for <strong>IBAP</strong> Diaries"))
        QtCore.QTimer.singleShot(18500, lambda: self.ui.label_loading.setText("<strong>Loading</strong> Log In Screen..."))
        # display splashscreen
        self.show()


    def progress(self):

        global counter

        # Set a value in the progress bar
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.qTimer.stop()

            # Show next window
            #self.main = MainWindow()
            #self.main.show()


            # Close Splashscreen
            self.close()

        # increase counter
        counter += 1


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
