# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
'''
COE116L-A1-GROUP7

GARCIA, MIECAELA VANESSA
MARTINEZ, KRISHA RAIN
RODRIGO, TIFFANY

PassionEAT Sign Up Window
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(358, 287)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/store.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignUpWindow.setWindowIcon(icon)
        self.UsernameSU = QtWidgets.QLabel(SignUpWindow)
        self.UsernameSU.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.UsernameSU.setObjectName("UsernameSU")
        self.PasswordSU = QtWidgets.QLabel(SignUpWindow)
        self.PasswordSU.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.PasswordSU.setObjectName("PasswordSU")
        self.FullNameSU = QtWidgets.QLabel(SignUpWindow)
        self.FullNameSU.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.FullNameSU.setObjectName("FullNameSU")
        self.EmailSU = QtWidgets.QLabel(SignUpWindow)
        self.EmailSU.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.EmailSU.setObjectName("EmailSU")
        self.UsernameSave = QtWidgets.QLineEdit(SignUpWindow)
        self.UsernameSave.setGeometry(QtCore.QRect(110, 40, 191, 20))
        self.UsernameSave.setObjectName("UsernameSave")
        self.PasswordSave = QtWidgets.QLineEdit(SignUpWindow)
        self.PasswordSave.setGeometry(QtCore.QRect(110, 80, 191, 20))
        self.PasswordSave.setObjectName("PasswordSave")
        self.FullNameSave = QtWidgets.QLineEdit(SignUpWindow)
        self.FullNameSave.setGeometry(QtCore.QRect(110, 120, 191, 20))
        self.FullNameSave.setObjectName("FullNameSave")
        self.EmailSave = QtWidgets.QLineEdit(SignUpWindow)
        self.EmailSave.setGeometry(QtCore.QRect(110, 160, 191, 20))
        self.EmailSave.setObjectName("EmailSave")
        self.SignUpSave = QtWidgets.QPushButton(SignUpWindow)
        self.SignUpSave.setGeometry(QtCore.QRect(160, 200, 75, 23))
        self.SignUpSave.setObjectName("SignUpSave")
       

        
        '''
        BUTTON
        '''
        self.SignUpSave.clicked.connect(self.SignUpFunc)
        
        
        self.retranslateUi(SignUpWindow)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "PassionEAT Sign Up"))
        self.UsernameSU.setText(_translate("SignUpWindow", "Username"))
        self.PasswordSU.setText(_translate("SignUpWindow", "Password"))
        self.FullNameSU.setText(_translate("SignUpWindow", "Full Name"))
        self.EmailSU.setText(_translate("SignUpWindow", "Email Address"))
        self.SignUpSave.setText(_translate("SignUpWindow", "Sign Up"))
        
        

    '''
    SIGN UP
    '''
  
    def SignUpFunc(self):
        user = self.UsernameSave.text()
        passw = self.PasswordSave.text()
        fulln = self.FullNameSave.text()
        email = self.EmailSave.text()
        profile = user + ";" + passw + ";" + fulln + ";" + email
        f1= open("accounts.txt","a")
        f1.write(profile + "\n" )
        print("SAVED!")


        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpWindow = QtWidgets.QWidget()
    ui = Ui_SignUpWindow()
    ui.setupUi(SignUpWindow)
    SignUpWindow.show()
    sys.exit(app.exec_())

