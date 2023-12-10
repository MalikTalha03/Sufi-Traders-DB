from PyQt6 import QtCore, QtGui, QtWidgets
from paymentsup import Ui_Form
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
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(390, 40, 113, 24))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 70, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 40, 101, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 40, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 10, 191, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
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
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 91, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 530, 80, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.payorder)
        self.lineEdit.returnPressed.connect(self.findorder)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Payment"))
        self.label_5.setText(_translate("MainWindow", "Total Amount"))
        self.label_3.setText(_translate("MainWindow", "Order No"))
        self.label_2.setText(_translate("MainWindow", "Amount Paid"))
        self.label_10.setText(_translate("MainWindow", "Remaining Amount"))
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
        self.label_4.setText(_translate("MainWindow", "Supplier Name"))
        self.pushButton.setText(_translate("MainWindow", "Pay"))
        
    def findorder(self):
        self.tableWidget.setRowCount(0)
        order_id = self.lineEdit.text()

        try:
            # Fetch information for display from Customer_Order_Details and related tables
            query = """
                SELECT
                    COD.productID,
                    P.productName,
                    COD.salePrice,
                    COD.quantity,
                    COD.salePrice * COD.quantity AS prodtot,
                    CO.orderDate,
                    CO.customerID
                FROM Customer_Order_Details AS COD
                JOIN Products AS P ON COD.productID = P.productID
                JOIN Customer_Order AS CO ON COD.orderID = CO.orderID
                WHERE COD.orderID = '{}'
            """.format(order_id)

            rows = self.db.execute_read_query(query)

            if rows:
                total = 0
                total_paid = 0
                customer_id = None

                for row in rows:
                    product_id, product_name, sale_price, quantity, prodtot, order_date, customer_id = row

                    # Populate tableWidget
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
                    self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(product_id)))
                    self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(product_name)))
                    self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(sale_price)))
                    self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(quantity)))
                    self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(prodtot)))

                    total += prodtot

                self.lineEdit_4.setText(str(total))

                # Fetch total paid from transactions
                query_total_paid = """
                    SELECT COALESCE(SUM(totalAmount), 0)
                    FROM Customer_Transactions
                    WHERE orderID = '{}' AND transactionType IN ('Cash', 'Bank Transfer')
                """.format(order_id)

                rows_total_paid = self.db.execute_read_query(query_total_paid)
                if rows_total_paid and rows_total_paid[0][0] is not None:
                    total_paid = rows_total_paid[0][0]

                self.lineEdit_3.setText(str(total_paid))

                remaining_amount = total - total_paid
                self.lineEdit_9.setText(str(remaining_amount))

                # Display customer details
                query_customer = """
                    SELECT custFName, custLName, customerContact
                    FROM Customers
                    WHERE customerID = '{}'
                """.format(customer_id)

                rows_customer = self.db.execute_read_query(query_customer)
                if rows_customer:
                    customer_fname, customer_lname, customer_contact = rows_customer[0]
                    self.lineEdit_2.setText("{} {}".format(customer_fname, customer_lname))
                    # Display customer details in other fields as needed

            else:
                self.handle_order_not_found()

        except Exception as e:
            print(f"Error: {e}")
            self.handle_order_not_found()

    def handle_order_not_found(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Order Not Found")
        msg_box.setText("Order {} not found or an error occurred.".format(self.lineEdit.text()))
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()
        # Clear fields and re-enable input
        self.cleardata()
        self.lineEdit.setEnabled(True)
        self.lineEdit.setFocus()


        
    def payorder(self):
        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.ui.setValues(self.lineEdit.text(), self.lineEdit_4.text(), self.lineEdit_9.text())
        self.win.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
