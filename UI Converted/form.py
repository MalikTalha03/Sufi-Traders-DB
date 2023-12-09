from PyQt6 import QtCore, QtGui, QtWidgets
from topbar import MenuBar
from db import DatabaseManager
class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.row_details = []
        self.category_data = {}
        self.order_id = 0
        self.total = 0.0  
        self.customerinfo = {} 
        self.custindata = False
        self.db = DatabaseManager()
        self.orderid()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 70, 113, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 70, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(640, 70, 113, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(640, 10, 113, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 10, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 70, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 40, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 70, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 761, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(761, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 530, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 40, 71, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(400, 40, 113, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.lineEdit_4.returnPressed.connect(lambda: self.lineEdit_5.setFocus())
        self.lineEdit_5.returnPressed.connect(self.addNewRow)
        self.lineEdit_3.returnPressed.connect(self.handle_lineEdit3_enter) 
        self.lineEdit.returnPressed.connect(lambda: self.lineEdit_2.setFocus())
        self.lineEdit_2.returnPressed.connect(lambda: self.lineEdit_4.setFocus())
        self.lineEdit_6.setText(str(self.order_id))
        self.lineEdit_3.setFocus()
        self.lineEdit_8.setEnabled(False)
        self.pushButton.clicked.connect(self.opennextwin)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Order"))
        self.label_7.setText(_translate("MainWindow", "Order ID"))
        self.label_5.setText(_translate("MainWindow", "Product Name"))
        self.label_8.setText(_translate("MainWindow", "Total"))
        self.label_2.setText(_translate("MainWindow", "Contact No."))
        self.label_3.setText(_translate("MainWindow", "First name"))
        self.label_6.setText(_translate("MainWindow", "Quantity"))
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
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Last name"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.label_9.setText(_translate("MainWindow", "Customer ID"))
    

    def orderid(self):
        query = "SELECT COALESCE(MAX(orderID), 0) + 1 FROM Customer_Order"
        rows = self.db.execute_read_query(query)
        if rows and rows[0][0] is not None:
            self.order_id = int(rows[0][0])
        else:
            self.order_id = 1

    def showMessageBox(self, title, message, icon=QtWidgets.QMessageBox.Icon.Critical):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()

    def addNewRow(self):
        if not self.lineEdit_4.text():
            self.showMessageBox("Error", "Please enter product name")
            return
        elif not self.lineEdit_5.text():
            self.showMessageBox("Error", "Please enter quantity")
            return
        elif not self.lineEdit_5.text().isdigit():
            self.showMessageBox("Error", "Please enter valid quantity")
            return
        product_name = self.lineEdit_4.text()
        quantity = self.lineEdit_5.text()
        rows = self.db.execute_read_query("SELECT * FROM Products WHERE productName = '{}'".format(product_name))
        if rows:
            for row in rows:
                if int(quantity) <= row[5]:
                    for row_num in range(self.tableWidget.rowCount()):
                        if self.tableWidget.item(row_num, 0).text() == str(row[0]):
                            current_quantity = int(self.tableWidget.item(row_num, 3).text())
                            new_quantity = current_quantity + int(quantity)
                            if new_quantity <= row[5]:
                                self.tableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(new_quantity)))
                                product_price = row[2]
                                total_price = float(product_price * new_quantity)
                                self.tableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(total_price)))
                                self.total += float(product_price * int(quantity))
                                self.lineEdit_7.setText(str(self.total))
                                for detail in self.row_details:
                                    if detail['pid'] == row[0]:
                                        detail['quantity'] = new_quantity
                                        detail['total_price'] = total_price
                                self.lineEdit_5.clear()
                                self.lineEdit_4.clear()
                                self.lineEdit_4.setFocus()
                                return
                            else:
                                self.showStockIssueMessageBox(row[5])
                                return
                    self.addNewProductRow(row, quantity)
                else:
                    self.showStockIssueMessageBox(row[5])
        else:
            self.showMessageBox("Error", "No Product found against Name: {}".format(product_name))


    def showStockIssueMessageBox(self, available_quantity):
        self.showMessageBox("Error", f"Not enough stock available. Available quantity: {available_quantity}")

    def addNewProductRow(self, product_row, quantity):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(product_row[0])))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(product_row[1])))
        self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(quantity))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(product_row[2])))
        product_price = product_row[2] 
        total_price = product_price * int(quantity)
        self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(total_price)))
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row_position, col)
            if item:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
        delete_button = QtWidgets.QPushButton('Delete', self.tableWidget)
        delete_button.clicked.connect(lambda _, row=row_position: self.deleteRow(row))
        self.tableWidget.setCellWidget(row_position, 5, delete_button)
        self.total += float(product_price * int(quantity))
        self.lineEdit_7.setText(str(self.total))
        row_detail = {
            'pid': product_row[0],
            'pname': product_row[1],
            'quantity': quantity,
            'total_price': total_price,
            'price': product_row[2]
        }
        self.row_details.append(row_detail)
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.lineEdit_4.setFocus()

    def deleteRow(self, row):
        if 0 <= row < self.tableWidget.rowCount():
            quantity = int(self.tableWidget.item(row, 3).text())
            price = float(self.tableWidget.item(row, 2).text())
            self.total -= float(quantity * price)
            self.lineEdit_7.setText(str(self.total))
            self.tableWidget.removeRow(row)
            if 0 <= row < len(self.row_details):
                del self.row_details[row]

    def handle_lineEdit3_enter(self):
        phone = self.lineEdit_3.text()
        rows = self.db.execute_read_query("SELECT * FROM Customers WHERE customerContact = '{}'".format(phone))
        if rows:
            for row in rows:
                self.lineEdit.setText(row[1])
                self.lineEdit_2.setText(row[2])
                self.lineEdit_8.setText(str(row[0]))
                self.lineEdit.setEnabled(False)
                self.lineEdit_2.setEnabled(False)
                self.lineEdit_8.setEnabled(False)
                self.lineEdit_4.setFocus()
                self.custindata = True
        else:
            self.lineEdit.setFocus()

    def opennextwin(self):
        contact_number = self.lineEdit_3.text()
        if not contact_number:
            self.showMessageBox('Error',"Please Enter Contact Number")
            return
        elif len(contact_number) != 11:
            self.showMessageBox('Error',"Please Enter Valid Contact Number")
            return
        elif not self.lineEdit.text():
            self.showMessageBox('Error',"Please Enter First Name")
            return
        elif self.tableWidget.rowCount() == 0:
            self.showMessageBox('Error',"Please Enter Product")
            return
        self.customerinfo = {
            'fname': self.lineEdit.text(),
            'lname': self.lineEdit_2.text(),
            'phone': contact_number
        }
        from orderdetail import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.ui.setValues(self.row_details, self.order_id, self.lineEdit_8.text(), self.total, self.customerinfo, self.custindata)
        self.win.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
