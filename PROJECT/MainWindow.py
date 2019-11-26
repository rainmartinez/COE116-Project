# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
'''
COE116L-A1-GROUP7

GARCIA, MIECAELA VANESSA
MARTINEZ, KRISHA RAIN
RODRIGO, TIFFANY

PassionEAT Main Window
'''


from PyQt5 import QtCore, QtGui, QtWidgets

from LogInWindow import Ui_LogInWindow

#from functools import partial

from ProfileWindow import Ui_ProfileWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/store.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.Tab = QtWidgets.QTabWidget(MainWindow)
        self.Tab.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.Tab.setObjectName("Tab")
        self.Newsfeed = QtWidgets.QWidget()
        self.Newsfeed.setObjectName("Newsfeed")
        self.LOnewsfeed = QtWidgets.QPushButton(self.Newsfeed)
        self.LOnewsfeed.setGeometry(QtCore.QRect(540, 0, 75, 23))
        self.LOnewsfeed.setObjectName("LOnewsfeed")
        self.Ninput = QtWidgets.QPlainTextEdit(self.Newsfeed)
        self.Ninput.setGeometry(QtCore.QRect(10, 50, 521, 41))
        self.Ninput.setObjectName("Ninput")
        self.Post = QtWidgets.QPushButton(self.Newsfeed)
        self.Post.setGeometry(QtCore.QRect(540, 50, 61, 41))
        self.Post.setDefault(True)
        self.Post.setObjectName("Post")
        self.labelPost = QtWidgets.QLabel(self.Newsfeed)
        self.labelPost.setGeometry(QtCore.QRect(10, 26, 151, 20))
        self.labelPost.setObjectName("labelPost")
        self.Noutput = QtWidgets.QTextEdit(self.Newsfeed)
        self.Noutput.setGeometry(QtCore.QRect(10, 100, 591, 331))
        self.Noutput.setReadOnly(True)
        self.Noutput.setObjectName("Noutput")
        self.PRnewsfeed = QtWidgets.QPushButton(self.Newsfeed)
        self.PRnewsfeed.setGeometry(QtCore.QRect(460, 0, 75, 23))
        self.PRnewsfeed.setObjectName("PRnewsfeed")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/cutlery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Tab.addTab(self.Newsfeed, icon1, "")
        self.Forum = QtWidgets.QWidget()
        self.Forum.setObjectName("Forum")
        self.TabForum = QtWidgets.QTabWidget(self.Forum)
        self.TabForum.setGeometry(QtCore.QRect(0, 0, 621, 431))
        self.TabForum.setObjectName("TabForum")
        self.Recipes = QtWidgets.QWidget()
        self.Recipes.setObjectName("Recipes")
        self.RecList = QtWidgets.QListWidget(self.Recipes)
        self.RecList.setGeometry(QtCore.QRect(10, 90, 171, 311))
        self.RecList.setObjectName("RecList")
        self.RecInput = QtWidgets.QTextEdit(self.Recipes)
        self.RecInput.setGeometry(QtCore.QRect(10, 10, 511, 71))
        self.RecInput.setObjectName("RecInput")
        self.RecNew = QtWidgets.QPushButton(self.Recipes)
        self.RecNew.setGeometry(QtCore.QRect(530, 10, 75, 71))
        self.RecNew.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RecNew.setAutoFillBackground(False)
        icon = QtGui.QIcon.fromTheme("recipe")
        self.RecNew.setIcon(icon)
        self.RecNew.setObjectName("RecNew")
        self.RecReply = QtWidgets.QPushButton(self.Recipes)
        self.RecReply.setGeometry(QtCore.QRect(190, 370, 411, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/retweet-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RecReply.setIcon(icon2)
        self.RecReply.setObjectName("RecReply")
        self.RecOutput = QtWidgets.QTextEdit(self.Recipes)
        self.RecOutput.setGeometry(QtCore.QRect(190, 90, 411, 271))
        self.RecOutput.setReadOnly(False)
        self.RecOutput.setObjectName("RecOutput")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/recipe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TabForum.addTab(self.Recipes, icon3, "")
        self.Restaurants = QtWidgets.QWidget()
        self.Restaurants.setObjectName("Restaurants")
        self.ResReply = QtWidgets.QPushButton(self.Restaurants)
        self.ResReply.setGeometry(QtCore.QRect(190, 370, 411, 31))
        self.ResReply.setIcon(icon2)
        self.ResReply.setObjectName("ResReply")
        self.ResInput = QtWidgets.QTextEdit(self.Restaurants)
        self.ResInput.setGeometry(QtCore.QRect(10, 10, 511, 71))
        self.ResInput.setObjectName("ResInput")
        self.ResList = QtWidgets.QListWidget(self.Restaurants)
        self.ResList.setGeometry(QtCore.QRect(10, 90, 171, 311))
        self.ResList.setObjectName("ResList")
        self.ResNew = QtWidgets.QPushButton(self.Restaurants)
        self.ResNew.setGeometry(QtCore.QRect(530, 10, 75, 71))
        self.ResNew.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ResNew.setAutoFillBackground(False)
        icon = QtGui.QIcon.fromTheme("recipe")
        self.ResNew.setIcon(icon)
        self.ResNew.setObjectName("ResNew")
        self.ResOutput = QtWidgets.QTextEdit(self.Restaurants)
        self.ResOutput.setGeometry(QtCore.QRect(190, 90, 411, 271))
        self.ResOutput.setReadOnly(False)
        self.ResOutput.setObjectName("ResOutput")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/restaurant (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TabForum.addTab(self.Restaurants, icon4, "")
        self.Suggestions = QtWidgets.QWidget()
        self.Suggestions.setObjectName("Suggestions")
        self.SugNew = QtWidgets.QPushButton(self.Suggestions)
        self.SugNew.setGeometry(QtCore.QRect(530, 10, 75, 71))
        self.SugNew.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SugNew.setAutoFillBackground(False)
        icon = QtGui.QIcon.fromTheme("recipe")
        self.SugNew.setIcon(icon)
        self.SugNew.setObjectName("SugNew")
        self.SugInput = QtWidgets.QTextEdit(self.Suggestions)
        self.SugInput.setGeometry(QtCore.QRect(10, 10, 511, 71))
        self.SugInput.setObjectName("SugInput")
        self.SugReply = QtWidgets.QPushButton(self.Suggestions)
        self.SugReply.setGeometry(QtCore.QRect(190, 370, 411, 31))
        self.SugReply.setIcon(icon2)
        self.SugReply.setObjectName("SugReply")
        self.SugList = QtWidgets.QListWidget(self.Suggestions)
        self.SugList.setGeometry(QtCore.QRect(10, 90, 171, 311))
        self.SugList.setObjectName("SugList")
        self.SugOutput = QtWidgets.QTextEdit(self.Suggestions)
        self.SugOutput.setGeometry(QtCore.QRect(190, 90, 411, 271))
        self.SugOutput.setObjectName("SugOutput")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/restaurant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TabForum.addTab(self.Suggestions, icon5, "")
        self.PRforum = QtWidgets.QPushButton(self.Forum)
        self.PRforum.setGeometry(QtCore.QRect(460, 0, 75, 23))
        self.PRforum.setObjectName("PRforum")
        self.LOForum = QtWidgets.QPushButton(self.Forum)
        self.LOForum.setGeometry(QtCore.QRect(540, 0, 75, 23))
        self.LOForum.setObjectName("LOForum")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/stand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Tab.addTab(self.Forum, icon6, "")
        self.Community = QtWidgets.QWidget()
        self.Community.setObjectName("Community")
        self.LOcommunity = QtWidgets.QPushButton(self.Community)
        self.LOcommunity.setGeometry(QtCore.QRect(540, 0, 75, 23))
        self.LOcommunity.setObjectName("LOcommunity")
        self.PRcommunity = QtWidgets.QPushButton(self.Community)
        self.PRcommunity.setGeometry(QtCore.QRect(460, 0, 75, 23))
        self.PRcommunity.setObjectName("PRcommunity")
        self.ComList = QtWidgets.QListWidget(self.Community)
        self.ComList.setGeometry(QtCore.QRect(160, 50, 271, 361))
        self.ComList.setObjectName("ComList")
        self.ComUsers = QtWidgets.QLabel(self.Community)
        self.ComUsers.setGeometry(QtCore.QRect(160, 30, 151, 20))
        self.ComUsers.setObjectName("ComUsers")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/gingerbread-man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Tab.addTab(self.Community, icon7, "")
        self.Welcome = QtWidgets.QLabel(MainWindow)
        self.Welcome.setGeometry(QtCore.QRect(470, 0, 141, 31))
        self.Welcome.setObjectName("Welcome")

        
        '''
        MAIN WINDOW BUTTONS
        '''
        self.LOnewsfeed.clicked.connect(self.LogOutClick)
        self.LOForum.clicked.connect(self.LogOutClick)
        self.LOcommunity.clicked.connect(self.LogOutClick)
        
        self.PRnewsfeed.clicked.connect(self.ProfileClick)
        self.PRforum.clicked.connect(self.ProfileClick)
        self.PRcommunity.clicked.connect(self.ProfileClick)
        
        self.Post.clicked.connect(self.NewsfeedClick)
        
        
        '''
        self.PRnewsfeed.clicked.connect(self.LogInClick)
        self.PRforum.clicked.connect(self.LogInClick)
        self.PRcommunity.clicked.connect(self.LogInClick)
        '''
        '''
        INSTANTIATE
        '''
        self.loginWindow = QtWidgets.QDialog(MainWindow)
        self.loginWindow.ui = Ui_LogInWindow()
        self.loginWindow.ui.setupUi(self.loginWindow)
        self.loginWindow.show()

        
        self.profileWindow = QtWidgets.QDialog(MainWindow)
        self.profileWindow.ui = Ui_ProfileWindow()
        self.profileWindow.ui.setupUi(self.profileWindow)
        

        '''
        LOG IN BUTTON
        '''
        self.loginWindow.ui.LogIn.clicked.connect(self.LogInClick)

        
        
        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        self.TabForum.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassionEAT"))
        self.LOnewsfeed.setText(_translate("MainWindow", "Log Out"))
        self.Post.setText(_translate("MainWindow", "Post"))
        self.labelPost.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">What\'s cooking?</span></p></body></html>"))
        self.PRnewsfeed.setText(_translate("MainWindow", "Profile"))
        self.Tab.setTabText(self.Tab.indexOf(self.Newsfeed), _translate("MainWindow", "Newsfeed"))
        self.RecNew.setText(_translate("MainWindow", "New Thread"))
        self.RecReply.setText(_translate("MainWindow", "Reply"))
        self.TabForum.setTabText(self.TabForum.indexOf(self.Recipes), _translate("MainWindow", "Recipes"))
        self.ResReply.setText(_translate("MainWindow", "Reply"))
        self.ResNew.setText(_translate("MainWindow", "New Thread"))
        self.TabForum.setTabText(self.TabForum.indexOf(self.Restaurants), _translate("MainWindow", "Restaurants"))
        self.SugNew.setText(_translate("MainWindow", "New Thread"))
        self.SugReply.setText(_translate("MainWindow", "Reply"))
        self.TabForum.setTabText(self.TabForum.indexOf(self.Suggestions), _translate("MainWindow", "Suggestions"))
        self.PRforum.setText(_translate("MainWindow", "Profile"))
        self.LOForum.setText(_translate("MainWindow", "Log Out"))
        self.Tab.setTabText(self.Tab.indexOf(self.Forum), _translate("MainWindow", "Forum"))
        self.LOcommunity.setText(_translate("MainWindow", "Log Out"))
        self.PRcommunity.setText(_translate("MainWindow", "Profile"))
        self.ComUsers.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Users</span></p><p><br/></p></body></html>"))
        self.Tab.setTabText(self.Tab.indexOf(self.Community), _translate("MainWindow", "Community"))
        self.Welcome.setText(_translate("MainWindow", "TextLabel"))

        
        
    '''
    LOG IN
    '''
    def LogInClick(self):
        print("test")
        user = self.loginWindow.ui.UsernameInput.text()
        passw = self.loginWindow.ui.PasswordInput.text()

        with open("accounts.txt", "r") as f:

            data = f.readlines()

            for line in data:
                lineZ = line.strip().split(";")
                print(lineZ)
                a = lineZ[0]
                b = lineZ[1]
                c = lineZ[2]
                d = lineZ[3]  

                if a == user and b == passw:
                    
                    '''
                    AYOS
                    '''
                    #self.loginWindow.ui.LogIn.clicked.connect(partial(self.NewsfeedClick, a))
                   
                    print("Success, it matches.")
                   
                    #hide Log in window
                    self.loginWindow.close()                  
                    self.loginWindow.ui.UsernameInput.clear()
                    self.loginWindow.ui.PasswordInput.clear()

                    #show main window
                    MainWindow.show()
                                         
                    #Welcome the user
                    self.Welcome.setText("Welcome, "+ c + "!\n" + d)
                    
                    #text file for ProfileWindow
                    f1= open(a + ".txt","w")
                    f1.close()
                    
                    
                    #name and email for ProfileWindow
                    self.profileWindow.ui.ProFullName.setText(c)
                    self.profileWindow.ui.ProEmail.setText(d)
                    
                     
                    break;
                else:
                    print("Failed.")
                    MainWindow.close()

                    
                   
                 
    '''
    LOG OUT
    '''   
    def LogOutClick(self):
        self.profileWindow.ui.ProFullName.clear()
        self.profileWindow.ui.ProEmail.clear()
        MainWindow.close()
        self.logInWindow.show()
        
        
        
    ''' 
    PROFILE
    '''    
    def ProfileClick(self):
        self.profileWindow.show()
        #ADD YUNG PARA SA TEXTEDIT
        
        
        
    '''
    COMMUNITY USERS
    '''            
    def ShowUsers(self):
        with open("accounts.txt", "r") as f:
            
            data = f.readlines()
            
            for line in data:
                lineZ = line.strip().split(";")
                a = lineZ[0]
                self.ComList.addItem(a)
                
                
    '''
    NEWSFEED
    '''
    def NewsfeedClick(self, kuhaA):
        
        Input = self.Ninput.toPlainText()
        
        with open("newsfeed.txt","a+") as f:
            
            #f.write(Input + "\n\n\n" )          #ADD THE NAME OF USER BEFORE "Input"
            self.Ninput.clear()
            f.seek(0)
            x = f.read()
            self.Noutput.setPlainText(x)
    
            f.close()
        '''   
        with open(kuhaA + ".txt","a+") as fu:        #CALL THE USERNAME FROM LOGINCLICK
            
            fu.write(Input + "\n\n\n" )      
        ''' 
          
   
        
        
  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    
    '''
    CALL ShowUsers
    '''
    ui.ShowUsers()
    '''
    ui.NewsfeedClick(ui.LogInClick())
    '''
    sys.exit(app.exec_())

