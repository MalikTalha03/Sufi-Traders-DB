# Form implementation generated from reading ui file 'orderdetail.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime
from paymentcust import Ui_MainWindow as payment

class Ui_MainWindow(object):
    def __init__(self, data,order,custid,total):
        self.total = total
        self.data = data
        self.cid=custid
        self.orderno=order
        self.populate_table()
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
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
        self.lineEdit_6.setEnabled(False)
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
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuoptions = QtWidgets.QMenu(parent=self.menubar)
        self.menuoptions.setObjectName("menuoptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionadd = QtGui.QAction(parent=MainWindow)
        self.actionadd.setObjectName("actionadd")
        self.menuoptions.addAction(self.actionadd)
        self.menubar.addAction(self.menuoptions.menuAction())
        self.pushButton.clicked.connect(self.addtodb)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
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
        self.menuoptions.setTitle(_translate("MainWindow", "options"))
        self.actionadd.setText(_translate("MainWindow", "add"))

    def populate_table(self):
        self.lineEdit_6.setText('{}'.format(self.orderno))
        self.lineEdit_7.setText('{}'.format(self.total))
    # Assuming that self.data is a list of dictionaries
        for row_num, row_data in enumerate(self.data):
            # Add a new row to the table widget
            self.tableWidget.insertRow(row_num)

            # Define the keys you want to access
            keys_to_access = ['pid', 'pname', 'price', 'quantity', 'total_price']

            # Loop through the keys and set the items using the keys
            for col_num, col_key in enumerate(keys_to_access):
                item = QtWidgets.QTableWidgetItem(str(row_data.get(col_key, '')))
                self.tableWidget.setItem(row_num, col_num, item)

    def addtodb(self):
        cnxn = None
        order_date = datetime.now().date().strftime('%Y-%m-%d')
        order_time = datetime.now().time().strftime('%H:%M:%S')
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("INSERT INTO Customer_Order (orderID, customerID, employeeID, orderDate, orderTime) VALUES (?, ?, ?, ?, ?)",self.orderno, self.cid, 1, order_date, order_time)                
                for data in self.data:
                    # Check if the product already exists
                    cursor.execute(
                        "SELECT * FROM Products WHERE productID = ?", data['pid'])
                    existing_product = cursor.fetchone()

                    if existing_product is not None:
                        # Product already exists, update quantity or price
                        new_quantity = int(existing_product[5]) - int(data['quantity'])

                        cursor.execute(
                            "UPDATE Products SET inventory = ? WHERE productID = ?",
                            new_quantity, data['pid']
                        )
                        cursor.execute("Insert into Customer_Order_Details Values (?,?,?)",
                                       self.orderno,data['pid'],data['quantity'])
                cursor.commit()
            # Clear the list after successfully adding to the database
            self.openwin()
        
            self.total = 0
            self.data = []
            self.suppid=0
            self.orderno=0
            self.close()
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: ?",ex)
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            result = msg_box.exec_()
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()


    def openwin(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = payment()
        self.ui.setupUi(self.win)
        self.ui.setValues(self.orderno,self.total,self.cid)
        self.win.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
