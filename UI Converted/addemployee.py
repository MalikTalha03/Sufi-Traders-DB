from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
import hashlib
class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 391)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(68, 40, 71, 20))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 80, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 71, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 160, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 71, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 200, 113, 24))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 280, 71, 20))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 280, 72, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 300, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 240, 71, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 240, 113, 24))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 22))
        self.menubar.setObjectName("menubar")
        self.menuadd = QtWidgets.QMenu(parent=self.menubar)
        self.menuadd.setObjectName("menuadd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionoption = QtGui.QAction(parent=MainWindow)
        self.actionoption.setObjectName("actionoption")
        self.menuadd.addAction(self.actionoption)
        self.menubar.addAction(self.menuadd.menuAction())
        self.pushButton.clicked.connect(self.addemployee)
        self.lineEdit.returnPressed.connect(lambda: self.lineEdit_3.setFocus())
        self.lineEdit_2.returnPressed.connect(lambda: self.lineEdit_4.setFocus())
        self.lineEdit_3.returnPressed.connect(lambda: self.lineEdit_2.setFocus())
        self.lineEdit_4.returnPressed.connect(lambda: self.lineEdit_5.setFocus())
        self.lineEdit_5.returnPressed.connect(lambda: self.comboBox.setFocus())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Employee"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setText(_translate("MainWindow", "Contact Number"))
        self.label_3.setText(_translate("MainWindow", "Last Name"))
        self.label_4.setText(_translate("MainWindow", "Address"))
        self.label_5.setText(_translate("MainWindow", "Salary"))
        self.label_6.setText(_translate("MainWindow", "Type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Employee"))
        self.comboBox.setItemText(2, _translate("MainWindow", " CEO"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.menuadd.setTitle(_translate("MainWindow", "add"))
        self.actionoption.setText(_translate("MainWindow", "option"))

    def addemployee(self):
        if self.lineEdit_6.text() == '':
            msg = "Please enter a password"
            self.displaymsg(msg)
            return
        elif self.lineEdit_2.text() == '':
            msg = "Please enter a contact number"
            self.displaymsg(msg)
            return
        elif self.lineEdit_3.text() == '':
            msg = "Please enter a last name"
            self.displaymsg(msg)
            return
        elif self.lineEdit_4.text() == '':
            msg = "Please enter an address"
            self.displaymsg(msg)
            return
        elif self.lineEdit_5.text() == '':
            msg = "Please enter a salary"
            self.displaymsg(msg)
            return
        elif self.lineEdit.text() == '':
            msg = "Please enter a first name"
            self.displaymsg(msg)
            return
        
        fname = self.lineEdit.text()
        lname = self.lineEdit_3.text()
        contact = self.lineEdit_2.text()
        address = self.lineEdit_4.text()
        salary = self.lineEdit_5.text()
        typee =  self.comboBox.currentText()
        password = self.lineEdit_6.text()
        if fname == "" or lname == "" or contact == "" or address == "" or salary == "" or typee == "" or password == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill all the details")
            return
        hashedpassword = hashlib.sha256(password.encode()).hexdigest()
        rows = self.db.execute_read_query("SELECT MAX(employeeID) FROM Employee ")
        for row in rows:
            if row and row[0] is not None:
                self.order_id = row[0] + 1
            else:
                self.order_id = 1
        self.db.execute_query("INSERT into Employee Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.order_id,fname,lname,contact,address,salary,typee,hashedpassword))
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Employee Added")
        msg_box.setText("Employee Added Successfully..")
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()
        MainWindow.close()

    def displaymsg(self,msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText('{}'.format(msg))
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
