# Form implementation generated from reading ui file 'custpay.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime

class Ui_Form(object):
    def __init__(self):
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=MALIK-TALHA;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
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
        cnxn = None
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
        try:
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                maxid = cursor.execute("SELECT MAX(transactionID) FROM Supplier_Transactions").fetchone()[0]
                if maxid == None:
                    maxid = 1
                else:
                    maxid = int(maxid) + 1
                cursor.execute(
                    "INSERT INTO Supplier_Transactions VALUES (?,?,?,?,?)",maxid,paymentmethod,amount,orderid,datetime.now().strftime("%Y-%m-%d"))
                cnxn.commit()
                if float(amount) == float(remaining):
                    cursor.execute("Update Supplier_Order SET paymentStatus = 'Paid' WHERE orderID = ?",orderid)
                else:
                    cursor.execute("Update Supplier_Order SET paymentStatus = 'Partially Paid' WHERE orderID = ?",orderid)
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Payment Completed")
                msg_box.setText("Payment Completed Successfully")
                msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                result = msg_box.exec()
                self.lineEdit_9.setText("")
                self.lineEdit_8.setText("")
                self.lineEdit_7.setText("")
                
        except pyodbc.Error as ex:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: {}".format(ex))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        finally:
            if cnxn:
                cnxn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
