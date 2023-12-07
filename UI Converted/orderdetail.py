from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime
from paymentcust import Ui_MainWindow as payment
from topbar import MenuBar
from db import DatabaseManager

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.total = 0
        self.data = {}
        self.cid=0
        self.orderno=0
        self.custindata = True
        self.custinfo = {}
        self.db = DatabaseManager()

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
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(lambda: self.addtodb())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Details"))
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
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)


    def addtodb(self):
        order_date = datetime.now().date().strftime('%Y-%m-%d')
        order_time = datetime.now().time().strftime('%H:%M:%S')
        if self.custindata == False:
            rows = self.db.execute_read_query("Select MAX (customerID) from Customers")
            for row in rows:
                if row and row[0]:
                    self.cid = row[0] + 1
                else:
                    self.cid = 1
                self.db.execute_query("INSERT INTO Customers VALUES ({}, '{}', '{}', '{}')".format(self.cid,self.custinfo['fname'], self.custinfo['lname'], self.custinfo['phone']))  
        self.db.execute_query("INSERT INTO Customer_Order VALUES ('{}', '{}', 1, '{}', '{}','Credit')".format(self.orderno, self.cid, order_date, order_time))
        for data in self.data:
            # Check if the product already exists
            rows = self.db.execute_read_query("SELECT * FROM Products WHERE productID = '{}'".format(data['pid']))
            if rows:
                for row in rows:
                    existing_product = row
            if existing_product is not None:
                # Product already exists, update quantity or price
                new_quantity = int(existing_product[5]) - int(data['quantity'])

                self.db.execute_query("UPDATE Products SET inventory = {} WHERE productID = {}".format(new_quantity, data['pid']))
                self.db.execute_query("Insert into Customer_Order_Details Values ({},{},{},{})".format(self.orderno,data['pid'],data['quantity'],data['price']))
        # clear all fields
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.openwin()
        self.close()        
    def openwin(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = payment()
        self.ui.setupUi(self.win)
        self.ui.setValues(self.orderno,self.total,self.cid)
        self.win.show()
        

    def setValues(self,data,order,custid,total,custinfo,custindata):
        self.total = total
        self.data = data
        self.cid=custid
        self.orderno=order
        self.custinfo = custinfo
        self.custindata = custindata
        self.populate_table()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
