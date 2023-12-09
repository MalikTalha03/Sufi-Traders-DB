from PyQt6 import QtCore, QtGui, QtWidgets
from topbar import MenuBar
from db import DatabaseManager

class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 40, 113, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 70, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 40, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 40, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 10, 191, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 761, 431))
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
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(390, 70, 113, 24))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 70, 101, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(639, 530, 111, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit.returnPressed.connect(self.findorder)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Customer Order"))
        self.label_4.setText(_translate("MainWindow", "Customer Name"))
        self.label_9.setText(_translate("MainWindow", "Customer ID"))
        self.label_3.setText(_translate("MainWindow", "Order No"))
        self.label_2.setText(_translate("MainWindow", "Amount Paid"))
        self.label_5.setText(_translate("MainWindow", "Total Amount"))
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
        self.label_10.setText(_translate("MainWindow", "Remaining Amount"))
        self.pushButton.setText(_translate("MainWindow", "Receive Payment"))

    def findorder(self):
        self.clearfields()
        order_id = self.lineEdit.text()
        total = 0
        total_paid = 0
        order_rows = self.db.execute_read_query(
            "SELECT * FROM Customer_Order WHERE orderID = '{}'".format(order_id)
        )
        if not order_rows:
            self.show_order_not_found_error(order_id)
            return
        for order_row in order_rows:
            customer_id = order_row[1]
            self.lineEdit_8.setText(str(customer_id))
            customer_rows = self.db.execute_read_query(
                "SELECT * FROM Customers WHERE customerID = '{}'".format(customer_id)
            )
            if customer_rows:
                customer_name = "{} {}".format(customer_rows[0][1], customer_rows[0][2])
                self.lineEdit_2.setText(customer_name)
            product_rows = self.db.execute_read_query(
                """
                SELECT COD.productID, P.productName, P.salePrice, COD.quantity, (COD.quantity * P.salePrice) AS prodtot
                FROM Customer_Order_Details COD
                JOIN Products P ON COD.productID = P.productID
                WHERE COD.orderID = '{}'
                """.format(order_id)
            )
            for product_row in product_rows:
                total += product_row[4]
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for col in range(self.tableWidget.columnCount()):
                    self.tableWidget.setItem(
                        row_position, col, QtWidgets.QTableWidgetItem(str(product_row[col]))
                    )
                    if col == 4:
                        self.tableWidget.item(row_position, col).setFlags(
                            QtCore.Qt.ItemFlag.ItemIsEditable
                        )
            self.lineEdit_4.setText(str(total))
            transaction_rows = self.db.execute_read_query(
                """
                SELECT SUM(totalAmount)
                FROM Customer_Transactions
                WHERE orderID = '{}' AND transactionType IN ('Cash', 'Bank Transfer')
                """.format(order_id)
            )
            if transaction_rows and transaction_rows[0][0] is not None:
                total_paid = float(transaction_rows[0][0])
            self.lineEdit_3.setText(str(total_paid))
            remaining_amount = float(total) - total_paid
            self.lineEdit_9.setText(str(remaining_amount))

    def show_order_not_found_error(self, order_id):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Order Error")
        msg_box.setText("No Order Found against ID: {}".format(order_id))
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()

    def clearfields(self):
        self.lineEdit_2.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.tableWidget.setRowCount(0)

    def setvalues(self,orderno):
        self.lineEdit.setText(str(orderno))
        self.findorder()
        self.lineEdit.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
