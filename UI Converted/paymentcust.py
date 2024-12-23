from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from db import DatabaseManager
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.orderno = 0
        self.total = 0
        self.cid = 0
        self.db = DatabaseManager()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 324)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 170, 101, 16))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 130, 71, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 70, 113, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 130, 71, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 80, 71, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 170, 72, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 80, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.payment)
        self.lineEdit_6.returnPressed.connect(self.findorder)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Payment"))
        self.label.setText(_translate("MainWindow", "Payment Method"))
        self.label_9.setText(_translate("MainWindow", "Amount"))
        self.pushButton.setText(_translate("MainWindow", "Complete Payment"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Cash"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Credit"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bank Transfer"))
        self.label_7.setText(_translate("MainWindow", "Order ID"))
        self.label_8.setText(_translate("MainWindow", "Total"))

    def setValues(self,orderno,total,cid):
        self.orderno = orderno
        self.total = total
        self.cid = cid
        self.lineEdit_6.setText('{}'.format(self.orderno))
        self.lineEdit_7.setText('{}'.format(self.total))
        self.lineEdit_8.setText('{}'.format(self.total))
        self.lineEdit_6.setEnabled(False)
        self.comboBox.setFocus()

    def payment(self):
        payment_method = self.comboBox.currentText()
        entered_amount = float(self.lineEdit_8.text())
        if entered_amount == self.total:
            order_date = datetime.now().date().strftime('%Y-%m-%d')
            order_time = datetime.now().time().strftime('%H:%M:%S')
            rows = self.db.execute_read_query("SELECT MAX(transactionID) FROM Customer_Transactions")
            if rows :
                for row in rows:
                    if row and row[0]:
                        max_id = int(row[0])
                    else:
                        max_id = 0
            else:
                max_id = 0
            new_tid = max_id + 1
            self.db.execute_query("INSERT INTO Customer_Transactions VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(new_tid,payment_method,entered_amount,self.orderno,order_date,order_time ))
            self.db.execute_query("Update Customer_Order set paymentStatus = 'Paid' where orderID = '{}'".format(self.orderno))
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Payment Successful")
            msg_box.setText("Payment completed successfully.")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        elif entered_amount < self.total:
            rows = self.db.execute_read_query("SELECT * FROM Credit_Customers WHERE customerID = '{}'".format(self.cid))
            if rows:
                for row in rows:
                    credit_row = row
            if credit_row:
                updated_credit = float(credit_row[2]) + float(self.total - entered_amount) 
                self.db.execute_query("UPDATE Credit_Customers SET totalCredit = '{}' WHERE creditCustomerID = '{}'".format(updated_credit, credit_row[1]))
            else:
                rows = self.db.execute_read_query("SELECT MAX(creditCustomerID) FROM Credit_Customers")
                if rows:
                    for row in rows:
                        if row and row[0]:
                            max_id = int(row[0])
                        else:
                            max_id = 0
                else:
                    max_id = 0
                new_credit_customer_id = max_id + 1
                self.db.execute_query("INSERT INTO Credit_Customers VALUES ('{}', '{}', '{}')".format(new_credit_customer_id,self.cid, (self.total - entered_amount)))
            order_date = datetime.now().date().strftime('%Y-%m-%d')
            order_time = datetime.now().time().strftime('%H:%M:%S')
            rows = self.db.execute_read_query("SELECT MAX(transactionID) FROM Customer_Transactions")
            if rows :
                for row in rows:
                    if row and row[0]:
                        max_id = int(row[0])
                    else:
                        max_id = 0
            else:
                max_id = 0
            new_tid = max_id + 1
            self.db.execute_query("INSERT INTO Customer_Transactions VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(new_tid,payment_method,entered_amount,self.orderno,order_date,order_time ))
            self.db.execute_query("Update Customer_Order set paymentStatus = 'Partially Paid' where orderID = '{}'".format(self.orderno))
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Payment Successful")
            msg_box.setText("Partial payment completed successfully.")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Payment Error")
            msg_box.setText("Entered amount exceeds the total.")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            self.lineEdit_8.setFocus()
            self.lineEdit_8.selectAll()
                
    def findorder(self):
        id = self.lineEdit_6.text()
        self.lineEdit_6.setEnabled(False)
        total = 0
        totalpaid = 0
        rows = self.db.execute_read_query("SELECT * FROM Customer_Order_Details WHERE orderID = '{}'".format(id))
        if rows:
            for row in rows:
                prodtot = 0
                pid=row[1]
                quantity= row[2]
                prodprice=row[3]
                prodtot = int(quantity) * int(prodprice)
                total = total + prodtot
        self.lineEdit_7.setText(str(total))
        rows = self.db.execute_read_query("SELECT * FROM Customer_Transactions WHERE orderID = '{}' AND transactionType IN ('Cash', 'Bank Transfer')".format(id))
        if rows:
            for row in rows:
                totalpaid = totalpaid + row[2]
        rem = total -totalpaid
        if rem == 0 :
            self.lineEdit_8.setText(str(rem))
            self.pushButton.setEnabled(False)
        else:
            self.lineEdit_8.setText(str(rem))   
        rows = self.db.execute_read_query("SELECT * FROM Customer_Order WHERE orderID = '{}'".format(id))
        if rows:
            for row in rows:
                self.cid = row[1]
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Order Not Found")
            msg_box.setText("Order not found.")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            self.lineEdit_6.setEnabled(True)
            self.lineEdit_6.setFocus()
        self.orderno = id
        self.total = total

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
