from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from topbar import MenuBar
class Ui_MainWindow(object):
    def __init__(self):
        self.row_details = []
        self.category_data = {}
        self.order_id = 0
        self.total = 0.0  # initialize total in the __init__ method
        self.customerinfo = {} 
        self.custindata = False
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=MALIK-TALHA;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
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
        self.lineEdit_4.returnPressed.connect(self.move)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        cnxn = None
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT MAX(orderID) FROM Customer_Order")
                row = cursor.fetchone()

                if row and row[0] is not None:
                    self.order_id = int(row[0]) + 1
                else:
                    # If the table is empty, start with order ID 1
                    self.order_id = 1

        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: {}".format(ex))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()

    def move(self):
        self.lineEdit_5.setFocus()

    def addNewRow(self):
    # Get data from line edits
        product_name = self.lineEdit_4.text()
        quantity = self.lineEdit_5.text()
        print(type(self.total))
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT * FROM Products WHERE productName = ?", product_name)
                row = cursor.fetchone()
                
                if row:
                    if int(quantity) <= row[5]:
                        for row_num in range(self.tableWidget.rowCount()):
                            if self.tableWidget.item(row_num, 0).text() == str(row[0]):
                                current_quantity = int(self.tableWidget.item(row_num, 3).text())
                                new_quantity = current_quantity + int(quantity)

                                if new_quantity <= row[5]:  # Check if there is enough stock available
                                    self.tableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(new_quantity)))

                                    product_price = row[2]  # price will be fetched from db
                                    total_price = float(product_price * new_quantity)
                                    self.tableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(total_price)))

                

                                    self.total += float(product_price * int(quantity))
                                    self.lineEdit_7.setText(str(self.total))

                                    for detail in self.row_details:
                                        if detail['pid'] == row[0]:
                                            detail['quantity'] = new_quantity
                                            detail['total_price'] = total_price
                                    for col in range(self.tableWidget.columnCount()):
                                        item = self.tableWidget.item(row_num, col)
                                        if item:
                                            item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)

                                    # Clear the line edits
                                    self.lineEdit_5.clear()
                                    self.lineEdit_4.clear()
                                    self.lineEdit_4.setFocus()
                                    return  # Exit the function since the product is already in the list
                                    

                                else:
                                    self.showStockIssueMessageBox(row[5])
                                    return  # Exit the function since there is not enough stock

                        # If the loop completes without returning, it means the product is not in the list
                        self.addNewProductRow(row, quantity)
                    else:
                        self.showStockIssueMessageBox(row[5])
                else:
                    msg_box = QtWidgets.QMessageBox()
                    msg_box.setWindowTitle("Error")
                    msg_box.setText("No Product found against Name: {}".format(product_name))
                    msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    result = msg_box.exec()
        except pyodbc.Error as ex:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: {}".format(ex))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()


    def addNewProductRow(self, row, quantity):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(row[0])))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(row[1])))
        self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(quantity))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(row[2])))
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row_position, col)
            if item:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)

        product_price = row[2]  # price will be fetched from db
        total_price = product_price * int(quantity)
        self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(total_price)))

        delete_button = QtWidgets.QPushButton('Delete', self.tableWidget)
        delete_button.clicked.connect(lambda _, row=row_position: self.deleteRow(row))
        self.tableWidget.setCellWidget(row_position, 5, delete_button)

        self.total += float(product_price * int(quantity))
        self.lineEdit_7.setText(str(self.total))

        row_detail = {
            'pid': row[0],
            'pname': row[1],
            'quantity': quantity,
            'total_price': total_price,
            'price': row[2]
        }
        self.row_details.append(row_detail)

        # Clear the line edits
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.lineEdit_4.setFocus()

    def deleteRow(self, row):
        # Get the quantity and price of the item to be deleted
        quantity = int(self.tableWidget.item(row, 3).text())
        price = float(self.tableWidget.item(row, 2).text())

        # Update total
        self.total -= float(quantity * price)
        self.lineEdit_7.setText(str(self.total))

        # Remove the row from the table
        self.tableWidget.removeRow(row)

        # Remove the corresponding entry from row_details
        del self.row_details[row]


    def showStockIssueMessageBox(self, available_stock):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Stock Issue")
        msg_box.setText("Stock Not available.\n{} pieces available in stock".format(available_stock))
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        result = msg_box.exec()
    def handle_lineEdit3_enter(self):
    # Initialize cnxn to None
        cnxn = None
        
        phone = self.lineEdit_3.text()
        
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT * FROM Customers WHERE customerContact = ?", phone)
                row = cursor.fetchone()
                if row:
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
        except pyodbc.Error as ex:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: {}".format(ex))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()

    def opennextwin(self):
        if(self.lineEdit_3.text() == ""):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Enter Contact Number")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            return
        elif(len(self.lineEdit_3.text()) != 11):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Enter Valid Contact Number")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            return
        elif(self.lineEdit.text() == ""):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Enter First Name")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            return
        elif(self.tableWidget.rowCount() == 0):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Enter Product")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            return
        else:
            self.customerinfo= {
                'fname': self.lineEdit.text(),
                'lname': self.lineEdit_2.text(),
                'phone': self.lineEdit_3.text()
            }
            from orderdetail import Ui_MainWindow
            self.win = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.win)
            self.ui.setValues(self.row_details,self.order_id,self.lineEdit_8.text(),self.total,self.customerinfo,self.custindata)
            self.win.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
