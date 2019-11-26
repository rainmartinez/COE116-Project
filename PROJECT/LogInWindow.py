# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogInWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
'''
COE116L-A1-GROUP7

GARCIA, MIECAELA VANESSA
MARTINEZ, KRISHA RAIN
RODRIGO, TIFFANY

PassionEAT Log In Window
'''

from PyQt5 import QtCore, QtGui, QtWidgets

from SignUpWindow import Ui_SignUpWindow
          

class Ui_LogInWindow(object):

    def setupUi(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(370, 292)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/store.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogInWindow.setWindowIcon(icon)
        self.UsernameL = QtWidgets.QLabel(LogInWindow)
        self.UsernameL.setGeometry(QtCore.QRect(70, 70, 47, 13))
        self.UsernameL.setObjectName("UsernameL")
        self.PasswordL = QtWidgets.QLabel(LogInWindow)
        self.PasswordL.setGeometry(QtCore.QRect(70, 110, 47, 13))
        self.PasswordL.setObjectName("PasswordL")
        self.UsernameInput = QtWidgets.QLineEdit(LogInWindow)
        self.UsernameInput.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(LogInWindow)
        self.PasswordInput.setGeometry(QtCore.QRect(140, 110, 113, 20))
        ################
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        ################
        self.PasswordInput.setObjectName("PasswordInput")
        self.LogIn = QtWidgets.QPushButton(LogInWindow)
        self.LogIn.setGeometry(QtCore.QRect(160, 140, 75, 23))
        self.LogIn.setObjectName("LogIn")
        self.SignUp = QtWidgets.QPushButton(LogInWindow)
        self.SignUp.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.SignUp.setObjectName("SignUp")
        self.NA = QtWidgets.QLabel(LogInWindow)
        self.NA.setGeometry(QtCore.QRect(70, 180, 111, 21))
        self.NA.setObjectName("NA")
        
      
        '''
        SIGN UP BUTTON
        '''
        self.SignUp.clicked.connect(self.SignUpClick)

        
        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

    def retranslateUi(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "PassionEAT Log In"))
        self.UsernameL.setText(_translate("LogInWindow", "Username"))
        self.PasswordL.setText(_translate("LogInWindow", "Password"))
        self.LogIn.setText(_translate("LogInWindow", "Log In"))
        self.SignUp.setText(_translate("LogInWindow", "Sign Up"))
        self.NA.setText(_translate("LogInWindow", "No account? Sign Up:"))

        
        
        
        
    '''
    SIGN UP      FIX
    '''
    def SignUpClick(self):
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = Ui_SignUpWindow()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

        
 



   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogInWindow = QtWidgets.QWidget()
    ui = Ui_LogInWindow()
    ui.setupUi(LogInWindow)
    LogInWindow.show()
    sys.exit(app.exec_())

