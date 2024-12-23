from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from topbar import MenuBar
from db import DatabaseManager
class Ui_MainWindow(object):
    def __init__(self):
        self.total = 0
        self.data = []
        self.suppid=0
        self.db = DatabaseManager()
        self.id = 0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 721, 471))
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
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 520, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 51, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 10, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_2.setFont(font)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 10, 51, 16))
        self.label_2.setObjectName("label_2")
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.pushButton.clicked.connect(self.addtodb)
        self.lineEdit.returnPressed.connect(self.findorder)
        self.lineEdit.setFocus()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supplier Order Details"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Order No"))
        self.label_2.setText(_translate("MainWindow", "Total"))
        
    def setvalues(self,order):
        self.orderno = order
        self.lineEdit.setText(str(self.orderno))
        self.lineEdit.setEnabled(False)
        self.findorder()

    def findorder(self):
        order_id = self.lineEdit.text()

        # Fetching main order details
        order_rows = self.db.execute_read_query(
            "SELECT orderID, supplierID, totalAmount FROM Supplier_Order WHERE orderID = '{}'".format(order_id)
        )

        if not order_rows or order_rows[0][0] is None:
            self.showMessageBox("Error", "Order Not Found")
            return
        
        order_data = order_rows[0]
        self.lineEdit.setEnabled(False)
        self.id, self.suppid, self.total = order_data[0], order_data[1], order_data[2]

        rows = self.db.execute_read_query("""
            SELECT sod.productID, c.categoryName, p.productName, sod.purchasePrice, sod.quantity, (sod.purchasePrice * sod.quantity) AS total
            FROM Supplier_Order_Details sod
            JOIN Products p ON sod.productID = p.productID
            JOIN Categories c ON p.categoryID = c.categoryID
            WHERE sod.orderID = '{}'
        """.format(order_id))
        total = sum(data[5] for data in rows)
        self.lineEdit_2.setText(str(total))
        self.data = [
            {'pid': data[0], 'cname': data[1], 'pname': data[2], 'purprice': data[3], 'inv': data[4], 'total_price': data[5]}
            for data in rows
        ]
        self.populate_table()
        self.pushButton.setEnabled(False)

    def showMessageBox(self, title, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()

    def orderno(self):
        rows = self.db.execute_read_query("Select * From Supplier_Order")
        if rows:
            for row in rows:
                if row[0] is not None:
                    self.id = int(row[0]) + 1
                else:
                    self.id = 1
        else:
            self.id = 1
        self.lineEdit.setText(str(self.id))
        self.lineEdit.setEnabled(False)

    def populate_table(self):
        for row_num, row_data in enumerate(self.data):
            self.tableWidget.insertRow(row_num)
            keys_to_access = ['pid', 'cname', 'pname', 'purprice', 'inv', 'total_price']
            for col_num, col_key in enumerate(keys_to_access):
                item = QtWidgets.QTableWidgetItem(str(row_data.get(col_key, '')))
                self.tableWidget.setItem(row_num, col_num, item)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row_num, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)

    def addtodb(self):
        rows = self.db.execute_query("Insert into Supplier_Order Values ('{}','{}','{}','{}','{}')".format(self.id,datetime.today().strftime('%Y-%m-%d'),self.suppid,self.total,'Not Paid'))
        for data in self.data:
            rows = self.db.execute_read_query("Select * From Products Where productID='{}'".format(data['pid']))
            if rows:
                for row in rows:
                    existing_product = row
            if existing_product is not None:
                new_quantity = existing_product[5] + data['inv']
                new_price = data['sale_price']
                self.db.execute_query("UPDATE Products SET inventory = '{}', salePrice = '{}' WHERE productID = '{}'".format(new_quantity, new_price, data['pid']))
                self.db.execute_query("Insert into Supplier_Order_Details Values ('{}','{}','{}','{}')".format(self.id,data['pid'],data['purprice'],data['inv']))
            else:
                self.db.execute_query("INSERT INTO Products VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(data['pid'], data['pname'], data['sale_price'],data['cid'], self.suppid, data['inv']))
                self.db.execute_query("Insert into Supplier_Order_Details Values ('{}','{}','{}','{}')".format(self.id,data['pid'],data['purprice'],data['inv']))
        self.total = 0
        self.data = []
        self.suppid=0
        self.orderno=0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_box.setText("Order Added Successfully")
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()

    def setValues(self,data,suppid,total):
        self.data = data
        self.suppid=suppid
        self.total=total
        self.populate_table()
        self.orderno()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
