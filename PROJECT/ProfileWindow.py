# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProfileWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
'''
COE116L-A1-GROUP7

GARCIA, MIECAELA VANESSA
MARTINEZ, KRISHA RAIN
RODRIGO, TIFFANY

PassionEAT Profile Window
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        ProfileWindow.setObjectName("ProfileWindow")
        ProfileWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/store.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProfileWindow.setWindowIcon(icon)
        self.ProFullName = QtWidgets.QLabel(ProfileWindow)
        self.ProFullName.setGeometry(QtCore.QRect(20, 30, 421, 41))
        self.ProFullName.setObjectName("ProFullName")
        self.ProEmail = QtWidgets.QLabel(ProfileWindow)
        self.ProEmail.setGeometry(QtCore.QRect(20, 80, 341, 21))
        self.ProEmail.setObjectName("ProEmail")
        self.PostsOutput = QtWidgets.QTextEdit(ProfileWindow)
        self.PostsOutput.setGeometry(QtCore.QRect(20, 170, 601, 291))
        self.PostsOutput.setReadOnly(True)
        self.PostsOutput.setObjectName("PostsOutput")
        self.ProPosts = QtWidgets.QLabel(ProfileWindow)
        self.ProPosts.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.ProPosts.setObjectName("ProPosts")
        

        self.retranslateUi(ProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileWindow)

    def retranslateUi(self, ProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileWindow.setWindowTitle(_translate("ProfileWindow", "PassionEAT Profile"))
        self.ProFullName.setText(_translate("ProfileWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.ProEmail.setText(_translate("ProfileWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">TextLabel</span></p></body></html>"))
        self.ProPosts.setText(_translate("ProfileWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Posts</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileWindow = QtWidgets.QWidget()
    ui = Ui_ProfileWindow()
    ui.setupUi(ProfileWindow)
    ProfileWindow.show()
    sys.exit(app.exec_())

