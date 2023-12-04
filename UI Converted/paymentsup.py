from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime
from db import DatabaseManager

class Ui_Form(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 50, 71, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(200, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(270, 40, 113, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 170, 101, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 100, 71, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 71, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 130, 71, 24))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(40, 130, 71, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_6.setEnabled(False)
        self.pushButton.clicked.connect(self.completepayment)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Total"))
        self.label_7.setText(_translate("Form", "Order ID"))
        self.label.setText(_translate("Form", "Payment Method"))
        self.comboBox.setItemText(0, _translate("Form", "Cash"))
        self.comboBox.setItemText(1, _translate("Form", "Bank Transfer"))
        self.label_9.setText(_translate("Form", "Remaining"))
        self.pushButton.setText(_translate("Form", "Complete Payment"))
        self.label_10.setText(_translate("Form", "Amount"))

    def setValues(self,orderid,total,remaining):
        self.lineEdit_6.setText(str(orderid))
        self.lineEdit_7.setText(str(total))
        self.lineEdit_8.setText(str(remaining))

    def completepayment(self):
        amount = self.lineEdit_9.text()
        orderid = self.lineEdit_6.text()
        remaining = self.lineEdit_8.text()
        paymentmethod = self.comboBox.currentText() 
        if amount == "":
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Enter Amount")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            return
        if float(amount) > float(remaining):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Amount cannot be greater than remaining amount")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            return
        rows = self.db.fetch("SELECT MAX(transactionID) FROM Supplier_Transactions")
        if rows:
            for row in rows:
                if row[0] == None:
                    maxid = 1
                else:
                    maxid = int(row[0]) + 1
        else:
            maxid = 1
        self.db.execute_query("INSERT INTO Supplier_Transactions VALUES ('{}','{}','{}','{}','{}')".format(maxid,paymentmethod,amount,orderid,datetime.now().strftime("%Y-%m-%d")))
        if float(amount) == float(remaining):
            self.db.execute_query("Update Supplier_Order SET paymentStatus = 'Paid' WHERE orderID = '{}'".format(orderid))
        else:
            self.db.execute_query("Update Supplier_Order SET paymentStatus = 'Partially Paid' WHERE orderID = '{}'".format(orderid))
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Payment Completed")
        msg_box.setText("Payment Completed Successfully")
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()
        self.lineEdit_9.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_7.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
