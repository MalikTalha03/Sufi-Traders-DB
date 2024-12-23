from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager

class Ui_Form(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(68, 110, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 190, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(68, 150, 91, 20))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(45, 20, 281, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 110, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(70, 230, 101, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 230, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 260, 91, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4.returnPressed.connect(self.findbycontact)
        self.lineEdit.returnPressed.connect(self.findbyid)
        self.lineEdit_4.setFocus()
        self.pushButton.clicked.connect(self.updatecustomer)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Update Customer Information"))
        self.label.setText(_translate("Form", "Customer ID"))
        self.label_2.setText(_translate("Form", "First Name"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Enter any of given requirment and press enter to find Customer Details</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Last Name"))
        self.label_4.setText(_translate("Form", "Customer Contact"))
        self.pushButton.setText(_translate("Form", "Update"))

    def findbyid(self):
        id = self.lineEdit.text()
        rows = self.db.execute_read_query("SELECT * FROM Customers WHERE customerID = '{}'".format(id))
        if rows:
            for row in rows:
                self.lineEdit_2.setText(row[1])
                self.lineEdit_3.setText(row[2])
                self.lineEdit_4.setText(row[3])
                self.lineEdit.setEnabled(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Customer Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
    def findbycontact(self):
        contact = self.lineEdit_4.text()
        rows = self.db.execute_read_query("SELECT * FROM Customers WHERE customerContact = '{}'".format(contact))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_2.setText(row[1])
                self.lineEdit_3.setText(row[2])
                self.lineEdit.setEnabled(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Customer Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
    def updatecustomer(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please Fill All Fields")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        id = self.lineEdit.text()
        fname = self.lineEdit_2.text()
        lname = self.lineEdit_3.text()
        contact = self.lineEdit_4.text()
        self.db.execute_query("UPDATE Customers SET custFName = '{}', custLName = '{}', customerContact = '{}' WHERE customerID = '{}'".format(fname, lname, contact, id))
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Customer Updated Successfully")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFocus()
        Form.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
