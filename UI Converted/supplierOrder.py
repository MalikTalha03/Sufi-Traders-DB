# Form implementation generated from reading ui file 'supplierOrder.ui'
#
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from supporderdetail import Ui_MainWindow as supporderdetail
from topbar import MenuBar
from db import DatabaseManager

class Ui_MainWindow(object):
    def __init__(self):
        self.total = 0  
        self.suppid = 0
        self.row_details = []
        self.category_data = {}
        self.db = DatabaseManager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 100, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 49, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 20, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 60, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 60, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 100, 113, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(510, 100, 113, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 140, 113, 24))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 190, 721, 341))
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
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(650, 120, 111, 41))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 530, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 140, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 20, 61, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(660, 50, 91, 24))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 140, 111, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit.returnPressed.connect(self.findsupplier)
        self.lineEdit_3.returnPressed.connect(self.findproduct)
        self.lineEdit_7.returnPressed.connect(self.addproduct)
        self.lineEdit_5.returnPressed.connect(lambda: self.lineEdit_6.setFocus())
        self.lineEdit_6.returnPressed.connect(lambda: self.lineEdit_7.setFocus())
        self.lineEdit_4.returnPressed.connect(lambda: self.lineEdit_5.setFocus())
        self.pushButton.clicked.connect(self.open_supplier_order_detail)
        self.fetch_and_populate_categories()
        self.comboBox.activated.connect(self.handle_category_selection)
        self.orderno()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supplier Order"))
        self.label.setText(_translate("MainWindow", "Supplier ID"))
        self.label_2.setText(_translate("MainWindow", "Supplier Name"))
        self.label_3.setText(_translate("MainWindow", "Product ID"))
        self.label_4.setText(_translate("MainWindow", "Product Name"))
        self.label_5.setText(_translate("MainWindow", "Purchase Price"))
        self.label_6.setText(_translate("MainWindow", "Sale Price"))
        self.label_7.setText(_translate("MainWindow", "Quantity"))
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
        self.label_8.setText(_translate("MainWindow", "Grand Total"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.label_9.setText(_translate("MainWindow", "Category"))
        self.label_10.setText(_translate("MainWindow", "OrderID"))

    def orderno(self):
        rows  = self.db.execute_read_query("Select MAX(orderID) From Supplier_Order")
        if rows:
            for row in rows:
                if row[0] is None:
                    self.id = 1
                else:
                    self.id = int(row[0]) + 1
        else:
            self.id = 1
        self.lineEdit_10.setText(str(self.id))

    def findsupplier(self):
        
        id = self.lineEdit.text()
        row = self.db.execute_read_query("SELECT * FROM Supplier WHERE supplierID = '{}'".format(id))
        if row:
            for row in row:
                self.lineEdit_2.setText(row[1])
                self.lineEdit_3.setFocus()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Supplier Error")
            msg_box.setText("Supplier Not Found. Please add supplier before proceeding.")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()

    def findproduct(self):
        pid = self.lineEdit_3.text()
        rows = self.db.execute_read_query("SELECT * FROM Products WHERE productID = '{}'".format(pid))
        if rows:
            for row in rows:
                self.lineEdit_4.setText(row[1])
                self.lineEdit_4.setEnabled(False)
                self.lineEdit_6.setText(str(row[2]))
                catid = row[3]
                catname = self.get_key_by_value(catid)
                index = self.comboBox.findText(catname)
                if index != -1:
                    self.comboBox.setCurrentIndex(index)
                    self.comboBox.setEnabled(False)
                self.lineEdit_5.setFocus()
        else:
            self.lineEdit_4.setFocus()

    def get_key_by_value(self,target_value):
        for key, value in self.category_data.items():
            if value == target_value:
                return key
        return None 

    def addproduct(self):
        if (
            self.lineEdit.text() and self.lineEdit_3.text() and self.lineEdit_4.text()
            and self.lineEdit_6.text() and self.lineEdit_7.text() and self.comboBox.currentIndex() >= 0):
            pid = self.lineEdit_3.text()
            pname = self.lineEdit_4.text()
            saleprice = float(self.lineEdit_6.text())
            inv = int(self.lineEdit_7.text())
            self.suppid = self.lineEdit.text()
            purprice = float(self.lineEdit_5.text())
            selected_category_name = self.comboBox.currentText()
            cid = self.category_data.get(selected_category_name, "Unknown Category")
            total_price = purprice * inv
            existing_product_index = -1
            for i, row_detail in enumerate(self.row_details):
                if row_detail['pid'] == pid:
                    existing_product_index = i
                    break
            if existing_product_index != -1:
                existing_inv = self.row_details[existing_product_index]['inv']
                self.row_details[existing_product_index]['inv'] += inv
                self.row_details[existing_product_index]['total_price'] += total_price
                self.tableWidget.setItem(existing_product_index, 4, QtWidgets.QTableWidgetItem(str(existing_inv + inv)))
                self.tableWidget.setItem(existing_product_index, 5, QtWidgets.QTableWidgetItem(str(self.row_details[existing_product_index]['total_price'])))
            else:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pid))
                self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(selected_category_name))
                self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(pname))
                self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(purprice)))
                self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(inv)))
                self.tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(total_price)))
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row_position, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                self.total += total_price
                self.lineEdit_8.setText(str(self.total))
                row_detail = {
                    'pid': pid,
                    'pname': pname,
                    'purprice': purprice,
                    'inv': inv,
                    'total_price': total_price,
                    'sale_price': saleprice,
                    'cid': cid,
                    'cname': selected_category_name,
                }
                self.row_details.append(row_detail)
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.comboBox.clear()
            self.lineEdit_4.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.fetch_and_populate_categories()
            self.lineEdit_3.setFocus()

    def fetch_and_populate_categories(self):
        rows = self.db.execute_read_query("SELECT * FROM Categories")
        if rows:
            self.category_data = {row[1]: row[0] for row in rows}
            for row in rows:
                category_name = row[1]
                self.comboBox.addItem(category_name)

    def handle_category_selection(self, index):
        selected_category_name = self.comboBox.currentText()
        selected_category_id = self.category_data.get(selected_category_name, None)

    def open_supplier_order_detail(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = supporderdetail()
        self.ui.setupUi(self.win)
        self.ui.setValues(self.row_details, self.suppid, self.total)
        self.win.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
