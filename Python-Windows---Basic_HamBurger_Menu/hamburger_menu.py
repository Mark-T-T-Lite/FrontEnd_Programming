'''
@Author: Mark_T
@Title: Main Hamburger menu template file
@version: 1.0.0.

# In pursuit of quicker DevOps
'''
# Import useful libraries
import sys, platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


from ui_hamburger_menu import Ui_MainWindow     # Access GUI code
from menuUI_functions import *          # Functions for interacting with the UI

# IMPORT QSS CUSTOM
#from ui_styles import Style

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Show some of the System details
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

    ########################################################################
    #Set the Window ATTRIBUTES
    ########################################################################
        MenuUI_Functions.removeTitleBar(True)       #Hide Window Title Bar

        # Put a Window Title
        self.setWindowTitle('App_Name')
        MenuUI_Functions.labelTitle(self, 'App_Name')
        MenuUI_Functions.labelDescription(self, 'Set text')
        

        # Default size for the window
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # MenuUI_Functions.enableMaximumSize(self, 500, 720)
    ########################################################################

        
    ########################################################################
    #Developing the Menus
    ########################################################################
        #Toggle menu width
        self.ui.btn_toggle_menu.clicked.connect(lambda: MenuUI_Functions.toggleMenu(self, 250, True))

        # #Adding Custom menus commented out
        self.ui.stackedWidget.setMinimumWidth(20)
        # MenuUI_Functions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        # MenuUI_Functions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        # MenuUI_Functions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        #Menu to start with and its page
        MenuUI_Functions.selectStandardMenu(self, "btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        #Show/Hide User Icon
        MenuUI_Functions.userIcon(self, "TM", "", True)
    ########################################################################


    ########################################################################
    #Function for moving or maximize or restoring  window
    ########################################################################
        def moveWindow(event):
            # If maximised, return to normal
            if MenuUI_Functions.returStatus() == 1:
                MenuUI_Functions.maximize_restore(self)

            # moving the window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
    ########################################################################

        # widget to be moved
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        MenuUI_Functions.uiDefinitions(self)        #Load Definitions of the UI
        

        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
 
        # Show the window now
        self.show()

########################################################################
## When a menu button is clicked
########################################################################
    def Button(self):
        # Recognise button clicked
        btnWidget = self.sender()

        # Change to Home Page
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            MenuUI_Functions.resetStyle(self, "btn_home")
            MenuUI_Functions.labelPage(self, "Home")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

        # Change to Now Playing
        if btnWidget.objectName() == "btn_play":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_play)
            MenuUI_Functions.resetStyle(self, "btn_play")
            #MenuUI_Functions.labelPage(self, "New User")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

        # Change to movies 
        if btnWidget.objectName() == "btn_movie":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_movie)
            MenuUI_Functions.resetStyle(self, "btn_movie")
            #MenuUI_Functions.labelPage(self, "New User")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

        # Change to Downloads
        if btnWidget.objectName() == "btn_downloads":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_download)
            MenuUI_Functions.resetStyle(self, "btn_downloads")
            #MenuUI_Functions.labelPage(self, "New User")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

        # Change to payments
        if btnWidget.objectName() == "btn_payments":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_payments)
            MenuUI_Functions.resetStyle(self, "btn_payments")
            #MenuUI_Functions.labelPage(self, "New User")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

        # User Profile
        if btnWidget.objectName() == "label_user_icon":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_user)
            MenuUI_Functions.resetStyle(self, "label_user_icon")
            #MenuUI_Functions.labelPage(self, "New User")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

        # Change to settings
        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            MenuUI_Functions.resetStyle(self, "btn_settings")
            #MenuUI_Functions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(MenuUI_Functions.selectMenu(btnWidget.styleSheet()))

    ########################################################################



    
########################################################################
#APP EVENTS
########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
   
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


# Execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
