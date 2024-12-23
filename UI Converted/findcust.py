from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
class Ui_Form(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(78, 130, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(78, 170, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 170, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 101, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 210, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit.returnPressed.connect(self.findbyid)
        self.lineEdit_2.returnPressed.connect(self.findbyname)
        self.lineEdit_3.returnPressed.connect(self.findbycontact)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Find Customer"))
        self.label.setText(_translate("Form", "Customer ID"))
        self.label_2.setText(_translate("Form", "Customer Name"))
        self.label_3.setText(_translate("Form", "Customer Contact"))
        self.label_4.setText(_translate("Form", "Enter ID or Name and Press Enter to retrieve Details"))

    def findbyid(self):
        id = self.lineEdit.text()
        rows = self.db.execute_read_query("SELECT * FROM Customers WHERE customerID = '{}'".format(id))
        if rows:
            for row in rows:
                self.lineEdit_2.setText(row[1] + " " + row[2])
                self.lineEdit_3.setText(row[3])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Customer Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
    def findbyname(self):
        name = self.lineEdit_2.text()
        firstname = name.split(" ")[0]
        lastname = name.split(" ")[1]
        rows = self.db.execute_read_query("SELECT * FROM Customers WHERE custFName = '{}' AND custLName = '{}'".format(firstname, lastname))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_3.setText(row[3])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Customer Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
    
    def findbycontact(self):
        contact = self.lineEdit_3.text()
        rows = self.db.execute_read_query("SELECT * FROM Customers WHERE customerContact = '{}'".format(contact))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_2.setText(row[1] + " " + row[2])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Customer Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
