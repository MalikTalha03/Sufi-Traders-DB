from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
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
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 113, 24))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 761, 431))
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
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 80, 113, 24))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 20, 191, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 50, 113, 24))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(290, 50, 81, 20))
        self.label_11.setObjectName("label_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(390, 50, 113, 24))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit.returnPressed.connect(self.findordersbyid)
        self.lineEdit_2.returnPressed.connect(self.findorderbyname)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Total Balance"))
        self.label_3.setText(_translate("MainWindow", "Supplier ID"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Order Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Order Total"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Payment Status"))
        self.label_9.setText(_translate("MainWindow", "Contact No"))
        self.label_4.setText(_translate("MainWindow", "Supplier Name"))
        self.label_11.setText(_translate("MainWindow", "Address"))

    def findordersbyid(self):
        id = self.lineEdit.text()
        rembal = 0
        rows = self.db.execute_read_query("Select * from Supplier where supplierID='{}'".format(id))
        if rows:
            for row in rows:
                self.lineEdit_2.setText(str(row[1]))
                self.lineEdit_8.setText(str(row[2]))
                self.lineEdit_10.setText(str(row[3]))
                self.tableWidget.setRowCount(0)
                rows2 = self.db.execute_read_query("Select * from Supplier_Order where supplierID='{}'".format(id))
                if rows2:
                    for row_pos,row2 in enumerate(rows2):
                        self.tableWidget.insertRow(row_pos)
                        self.tableWidget.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(row2[0])))
                        self.tableWidget.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(row2[1])))
                        self.tableWidget.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(row2[3])))
                        remaining_amount = self.calculateRemainingAmount(row2[0])
                        rembal += remaining_amount
                        self.lineEdit_9.setText(str(rembal))
                        if remaining_amount > 0:
                            self.tableWidget.setItem(row_pos, 3, QtWidgets.QTableWidgetItem("Unpaid"))
                        else:
                            self.tableWidget.setItem(row_pos, 3, QtWidgets.QTableWidgetItem("Paid"))
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("No record found against this ID: {}".format(id))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        
    def calculateRemainingAmount(self, order_id):
        total = self.db.execute_read_query("Select totalAmount from Supplier_Order where orderID='{}'".format(order_id))
        for row in total:
            total = row[0]
        paid = self.db.execute_read_query("Select sum(totalAmount) from Supplier_Transactions where orderID='{}'".format(order_id))
        for row in paid:
            paid = row[0]
        return total - paid
    
    def findorderbyname(self):
        name = self.lineEdit_2.text()
        rows = self.db.execute_read_query("Select * from Supplier where supplierName='{}'".format(name))
        if rows:
            for row in rows:
                id = row[0]
            self.lineEdit.setText(str(id))
            self.findordersbyid()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("No record found against this Name: {}".format(name))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
