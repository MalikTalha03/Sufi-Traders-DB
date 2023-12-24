from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
import hashlib
from datetime import datetime

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.db = DatabaseManager()
        self.empid = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 260, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 340, 221, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 150, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 430, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit.returnPressed.connect(lambda: self.lineEdit_2.setFocus())
        self.lineEdit_2.returnPressed.connect(lambda: self.pushButton.setFocus())
        self.pushButton.clicked.connect(self.login)
        self.checkloggedin()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Welcome "))
        self.label_4.setText(_translate("MainWindow", "Please Enter your Credentials to Login"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

    def login(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter both username and password")
            return
        username = self.lineEdit.text()
        fname = username.split(" ")[0]
        lname = username.split(" ")[1]
        password = self.lineEdit_2.text()
        rows = self.db.execute_read_query("SELECT * FROM Employee WHERE empFName = '{}' AND empLName = '{}'".format(fname, lname))
        if rows:
            for row in rows:
                if row[7] == hashlib.sha256(password.encode()).hexdigest():
                    
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Success")
                    msg.setText("Login Successful")
                    msg.exec()
                    max_id = self.db.execute_read_query("SELECT MAX(sessionID) FROM Employee_Session")[0][0]
                    if max_id == None:
                        max_id = 1
                    else:
                        max_id += 1
                    self.db.execute_query("Insert into Employee_Session values('{}', '{}', '{}', '{}', '{}', '{}','{}')".format(max_id,row[0],datetime.now().strftime("%Y-%m-%d %H:%M:%S"),datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'','Active',8*60))
                    self.opendashboard()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Incorrect Password")
                    msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Incorrect Username")
            msg.exec()
    def opendashboard(self):
        from Dashboard import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()
        self.close()
    def checkloggedin(self):
        rows = self.db.execute_read_query("SELECT * FROM Employee_Session WHERE currStatus = 'Active'")
        if rows:
            for row in rows:
                self.empid = row[1]
                return True
        else:
            return False
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    res = ui.checkloggedin()
    if res == False:
        MainWindow.show()
        sys.exit(app.exec())
    else:
        ui.opendashboard()
        sys.exit(app.exec())
