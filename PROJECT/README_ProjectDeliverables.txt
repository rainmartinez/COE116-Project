COE116L/A1
GROUP 7
GARCIA, MIECAELA VANESSA S.
MARTINEZ, KRISHA RAIN
RODRIGO, TIFFANY

PROJECT DELIVERABLES


>>>LogInMainWindow.py<<<

The function SignUpClick is responsible for opening the Ui_SignUpWindow.



>>>SignUpWindow.py<<<

The function SignUpFunc is responsible for the events inside the Ui_SignUpWindow.
It accepts the username, password, full name, and email; then stores the values inside the text file.



>>>MainWindow.py<<<

The function LogInClick is responsible for the events inside the Ui_LogInWindow.
It accepts the username and password of the user, and authenticates if it is a match.
If the log in is successfull, the main window will show, and the log in window will close.
This function is also used for making a personal text file for each user, that will be later used in the Ui_ProfileWindow.

The function LogOutClick is used to log out from the main window. If the log out button is clicked,
this function will enable the main window to close and return to the log in window.

The function ShowUsers is responsible in showing the list of users in the community tab.

The function NewsfeedClick is used in showing the contents of the newsfeed, and storing what the user has just posted in his personal text file.
