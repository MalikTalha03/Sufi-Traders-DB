from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from paymentcust import Ui_MainWindow as payment
from topbar import MenuBar
from db import DatabaseManager
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.total = 0
        self.data = {}
        self.orderno=0
        self.db = DatabaseManager()
        self.rowdet = []
        self.dupdata = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 520, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(570, 10, 113, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 30, 113, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 761, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(761, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit_6.returnPressed.connect(lambda: self.searchorder())
        self.pushButton.clicked.connect(lambda: self.updatedb())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Returns"))
        self.pushButton.setText(_translate("MainWindow", "Update"))
        self.label_8.setText(_translate("MainWindow", "Total"))
        self.label_7.setText(_translate("MainWindow", "Order ID"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Per unit Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total"))
        
    def searchorder(self):
        self.clearall()
        self.orderno = self.lineEdit_6.text()
        query = """
            SELECT COD.productID, P.productName, COD.quantity, COD.salePrice
            FROM Customer_Order_Details COD
            JOIN Products P ON COD.productID = P.productID
            WHERE COD.orderID = '{}'
        """.format(self.orderno)
        rows = self.db.execute_read_query(query)
        if rows:
            for row in rows:
                data = {'pid': row[0],'pname': row[1],'quantity': row[2],'price': row[3],'total_price': float(row[2] * row[3])}
                self.total += data['total_price']
                self.rowdet.append(data)
            self.data = self.rowdet
            self.dupdata = [entry.copy() for entry in self.data]
            self.populate_table()
            self.tableWidget.cellChanged.connect(lambda: self.updatedata())
            self.lineEdit_7.setText('{}'.format(self.total))
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Order ID not found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.exec()

    def clearall(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.lineEdit_7.clear()
        self.total = 0
        self.rowdet = []
        self.data = {}
        self.dupdata = {}

    def populate_table(self):
        self.lineEdit_6.setText('{}'.format(self.orderno))
        self.lineEdit_7.setText('{}'.format(self.total))
        for row_num, row_data in enumerate(self.data):
            self.tableWidget.insertRow(row_num)
            keys_to_access = ['pid', 'pname', 'price', 'quantity', 'total_price']
            for col_num, col_key in enumerate(keys_to_access):
                item = QtWidgets.QTableWidgetItem(str(row_data.get(col_key, '')))
                self.tableWidget.setItem(row_num, col_num, item)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row_num, col)
                if item and col != 3:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)

    def updatedata(self):
        self.total = 0
        for row_num in range(self.tableWidget.rowCount()):
            for col_num in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row_num, col_num)
                if item and col_num == 3:
                    if int(item.text()) > self.data[row_num]['quantity']:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Return Quantity cannot be greater than original quantity")
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                        msg.exec()
                        item.setText('{}'.format(self.dupdata[row_num]['quantity']))
                        return
                    else:
                        self.dupdata[row_num]['quantity'] = int(item.text())
                        self.dupdata[row_num]['total_price'] = float(item.text()) * float(self.dupdata[row_num]['price'])
                else:
                    continue
        self.total += sum([entry['total_price'] for entry in self.dupdata])
        self.lineEdit_7.setText('{}'.format(self.total))

    def updatedb(self):
        if self.total == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No changes made")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.exec()
            return
        credit = self.db.execute_read_query("SELECT paymentStatus FROM Customer_Order WHERE orderID = '{}'".format(self.orderno))[0][0]
        if credit == 'Credit':
            self.db.execute_query("UPDATE Customer_Order_Details SET quantity = '{}' WHERE orderID = '{}' AND productID = '{}'".format( (self.data['quantity'] - int(row['quantity'])), self.orderno, row['pid']))
            self.db.execute_query("UPDATE Products SET inventory = inventory + '{}' WHERE productID = '{}'".format(row['quantity'], row['pid']))
            cred = self.db.execute_read_query("SELECT totalCredit FROM Credit_Customers WHERE customerID = (SELECT customerID FROM Customer_Order WHERE orderID = '{}')".format(self.orderno))[0][0]
            if cred == None:
                cred = 0
            else:
                cred = float(cred)
            newcred = cred - self.total
            self.db.execute_query("UPDATE Credit_Customers SET totalCredit = '{}' WHERE customerID = (SELECT customerID FROM Customer_Order WHERE orderID = '{}')".format(newcred, self.orderno))
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Return Completed. No refund Issued.")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.exec()
            MainWindow.close()
            self.clearall()
            return
        elif credit == 'Partially Paid':
            totalpaid = self.db.execute_read_query("SELECT SUM(amountPaid) FROM Customer_Transactions WHERE orderID = '{}'".format(self.orderno))[0][0]
            if totalpaid == None:
                totalpaid = 0
            else:
                totalpaid = float(totalpaid)
            if totalpaid > self.total:
                self.db.execute_query("UPDATE Customer_Order_Details SET quantity = '{}' WHERE orderID = '{}' AND productID = '{}'".format( (self.data['quantity'] - int(row['quantity'])), self.orderno, row['pid']))
                self.db.execute_query("UPDATE Products SET inventory = inventory + '{}' WHERE productID = '{}'".format(row['quantity'], row['pid']))
                amounttorefund = totalpaid - self.total
                self.db.execute_query("Insert into Customer_Transactions (transactionID, transactionType, transactionDate, totalAmount, orderID, transactionTime ) values ('{}', '{}', '{}', '{}', '{}', '{}')".format(maxtid, 'Refund', datetime.now().strftime("%Y-%m-%d"), amounttorefund, self.orderno, datetime.now().strftime("%H:%M:%S")))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("Return Completed. Refund of Rs. {} has been initiated".format(amounttorefund)) 
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.exec()  
                MainWindow.close()
                self.clearall()
                return
            elif totalpaid < self.total:
                self.db.execute_query("UPDATE Customer_Order_Details SET quantity = '{}' WHERE orderID = '{}' AND productID = '{}'".format( (self.data['quantity'] - int(row['quantity'])), self.orderno, row['pid']))
                self.db.execute_query("UPDATE Products SET inventory = inventory + '{}' WHERE productID = '{}'".format(row['quantity'], row['pid']))
                amounttorefund =  totalpaid
                self.db.execute_query("Insert into Customer_Transactions (transactionID, transactionType, transactionDate, totalAmount, orderID, transactionTime ) values ('{}', '{}', '{}', '{}', '{}', '{}')".format(maxtid, 'Refund', datetime.now().strftime("%Y-%m-%d"), amounttorefund, self.orderno, datetime.now().strftime("%H:%M:%S")))
                cred = self.db.execute_read_query("SELECT totalCredit FROM Credit_Customers WHERE customerID = (SELECT customerID FROM Customer_Order WHERE orderID = '{}')".format(self.orderno))[0][0]
                if cred == None:
                    cred = 0
                else:
                    cred = float(cred)
                newcred = cred - (self.total - totalpaid)
                self.db.execute_query("UPDATE Credit_Customers SET totalCredit = '{}' WHERE customerID = (SELECT customerID FROM Customer_Order WHERE orderID = '{}')".format(newcred, self.orderno))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("Return Completed. Refund of Rs. {} has been initiated".format(amounttorefund))
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.exec()
                MainWindow.close()
                self.clearall()
                return
        elif credit == 'Paid':
            for row in self.dupdata:
                pid = row['pid']
                totalquantity = self.data[0]['quantity']
                self.db.execute_query("UPDATE Customer_Order_Details SET quantity = '{}' WHERE orderID = '{}' AND productID = '{}'".format( (totalquantity - int(row['quantity'])), self.orderno, row['pid']))
                self.db.execute_query("UPDATE Products SET inventory = inventory + '{}' WHERE productID = '{}'".format(row['quantity'], row['pid']))
            maxtid = self.db.execute_read_query("SELECT MAX(transactionID) FROM Customer_Transactions")[0][0]
            if maxtid == None:
                maxtid = 0
            else:
                maxtid = int(maxtid) + 1
            self.total = -(self.total)
            self.db.execute_query("Insert into Customer_Transactions (transactionID, transactionType, transactionDate, totalAmount, orderID, transactionTime ) values ('{}', '{}', '{}', '{}', '{}', '{}')".format(maxtid, 'Refund', datetime.now().strftime("%Y-%m-%d"), self.total, self.orderno, datetime.now().strftime("%H:%M:%S")))
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Refund of Rs. {} has been initiated".format(-(self.total)))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.exec()
            MainWindow.close()
            self.clearall()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
