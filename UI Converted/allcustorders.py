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
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 20, 191, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 50, 113, 24))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 761, 431))
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
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 113, 24))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 60, 101, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(390, 60, 113, 24))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        MainWindow.setCentralWidget(self.centralwidget)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.findordersbyid)
        self.lineEdit_2.returnPressed.connect(self.findordersbyname)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Customer Orders"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Order Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Order Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Order Total"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Payment Status"))
        self.label_3.setText(_translate("MainWindow", "Customer ID"))
        self.label_9.setText(_translate("MainWindow", "Contact No"))
        self.label_4.setText(_translate("MainWindow", "Customer Name"))
        self.label_10.setText(_translate("MainWindow", "Remaining Credit"))

    def findordersbyid(self):
        id = self.lineEdit.text()
        id = self.lineEdit.text()
        rows = self.db.execute_read_query("SELECT * FROM Customer_Order WHERE customerID = {}".format(id))
        if rows:
            self.tableWidget.setRowCount(0)
            rows2 = self.db.execute_read_query("Select * from Customers where customerID={}".format(id))
            if rows2:
                for row2 in rows2:
                    self.lineEdit_2.setText('{}'.format(row2[1] +" "+ row2[2]))
                    self.lineEdit_8.setText(str(row2[3]))
            for row_number , row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[3])))
                self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[4])))
                self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data[5])))
                
                rows3 = self.db.execute_read_query("SELECT SUM(quantity * salePrice) FROM Customer_Order_Details where orderID={}".format(row_data[0]))
                for row3 in rows3:
                    total = row3[0]
                self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(total)))
                rows4 = self.db.execute_read_query("Select * from Credit_Customers where customerID={}".format(id))
                if rows4:
                    for row4 in rows4:
                        self.lineEdit_9.setText(str(row4[2]))
                else:
                    self.lineEdit_9.setText('0')
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row_number, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                openbtn = QtWidgets.QPushButton('Open', self.tableWidget)
                openbtn.clicked.connect(lambda _, row=row_number: self.opendetail(row))
                self.tableWidget.setCellWidget(row_number, 5, openbtn)
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("No record found against this ID: {}".format(id))
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
        
    def findordersbyname(self):
        name = self.lineEdit_2.text()
        firstName = name.split()[0]
        lastName = name.split()[1]
        
        row = self.db.execute_read_query("SELECT * FROM Customers WHERE custFName = '{}' AND custLName = '{}'".format(firstName, lastName))
        if row:
            for row in row:
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

    def opendetail(self, row):
        from findcustorder import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.setvalues(self.tableWidget.item(row, 0).text())
        self.window.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
