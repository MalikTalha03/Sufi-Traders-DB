# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 80, 691, 331))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(230, 20, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuCustomer = QtWidgets.QMenu(parent=self.menubar)
        self.menuCustomer.setObjectName("menuCustomer")
        self.menuSupplier = QtWidgets.QMenu(parent=self.menubar)
        self.menuSupplier.setObjectName("menuSupplier")
        self.menuProduct = QtWidgets.QMenu(parent=self.menubar)
        self.menuProduct.setObjectName("menuProduct")
        self.menuEmployee = QtWidgets.QMenu(parent=self.menubar)
        self.menuEmployee.setObjectName("menuEmployee")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Order = QtGui.QAction(parent=MainWindow)
        self.actionNew_Order.setObjectName("actionNew_Order")
        self.actionGet_Paid = QtGui.QAction(parent=MainWindow)
        self.actionGet_Paid.setObjectName("actionGet_Paid")
        self.actionFind_Order = QtGui.QAction(parent=MainWindow)
        self.actionFind_Order.setObjectName("actionFind_Order")
        self.actionUpdate_Customer = QtGui.QAction(parent=MainWindow)
        self.actionUpdate_Customer.setObjectName("actionUpdate_Customer")
        self.actionGet_All_Orders = QtGui.QAction(parent=MainWindow)
        self.actionGet_All_Orders.setObjectName("actionGet_All_Orders")
        self.actionNew_Order_2 = QtGui.QAction(parent=MainWindow)
        self.actionNew_Order_2.setObjectName("actionNew_Order_2")
        self.actionPay_Supplier = QtGui.QAction(parent=MainWindow)
        self.actionPay_Supplier.setObjectName("actionPay_Supplier")
        self.actionFind_Supplier = QtGui.QAction(parent=MainWindow)
        self.actionFind_Supplier.setObjectName("actionFind_Supplier")
        self.actionUpdate_details = QtGui.QAction(parent=MainWindow)
        self.actionUpdate_details.setObjectName("actionUpdate_details")
        self.actionAll_Orderd = QtGui.QAction(parent=MainWindow)
        self.actionAll_Orderd.setObjectName("actionAll_Orderd")
        self.actionFind_Order_2 = QtGui.QAction(parent=MainWindow)
        self.actionFind_Order_2.setObjectName("actionFind_Order_2")
        self.actionInventory = QtGui.QAction(parent=MainWindow)
        self.actionInventory.setObjectName("actionInventory")
        self.actionAdd_Category = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Category.setObjectName("actionAdd_Category")
        self.actionAdd = QtGui.QAction(parent=MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionCheck_Details = QtGui.QAction(parent=MainWindow)
        self.actionCheck_Details.setObjectName("actionCheck_Details")
        self.actionUpdate_Details = QtGui.QAction(parent=MainWindow)
        self.actionUpdate_Details.setObjectName("actionUpdate_Details")
        self.actionDelete = QtGui.QAction(parent=MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuCustomer.addAction(self.actionNew_Order)
        self.menuCustomer.addAction(self.actionGet_Paid)
        self.menuCustomer.addAction(self.actionFind_Order)
        self.menuCustomer.addAction(self.actionUpdate_Customer)
        self.menuCustomer.addAction(self.actionGet_All_Orders)
        self.menuSupplier.addAction(self.actionNew_Order_2)
        self.menuSupplier.addAction(self.actionPay_Supplier)
        self.menuSupplier.addAction(self.actionFind_Supplier)
        self.menuSupplier.addAction(self.actionUpdate_details)
        self.menuSupplier.addAction(self.actionAll_Orderd)
        self.menuSupplier.addAction(self.actionFind_Order_2)
        self.menuProduct.addAction(self.actionInventory)
        self.menuProduct.addAction(self.actionAdd_Category)
        self.menuEmployee.addAction(self.actionAdd)
        self.menuEmployee.addAction(self.actionCheck_Details)
        self.menuEmployee.addAction(self.actionUpdate_Details)
        self.menuEmployee.addAction(self.actionDelete)
        self.menubar.addAction(self.menuCustomer.menuAction())
        self.menubar.addAction(self.menuSupplier.menuAction())
        self.menubar.addAction(self.menuProduct.menuAction())
        self.menubar.addAction(self.menuEmployee.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Today Sales"))
        self.menuCustomer.setTitle(_translate("MainWindow", "Customer"))
        self.menuSupplier.setTitle(_translate("MainWindow", "Supplier"))
        self.menuProduct.setTitle(_translate("MainWindow", "Product"))
        self.menuEmployee.setTitle(_translate("MainWindow", "Employee"))
        self.actionNew_Order.setText(_translate("MainWindow", "New Order"))
        self.actionGet_Paid.setText(_translate("MainWindow", "Get Paid"))
        self.actionFind_Order.setText(_translate("MainWindow", "Find Order"))
        self.actionUpdate_Customer.setText(_translate("MainWindow", "Update Customer"))
        self.actionGet_All_Orders.setText(_translate("MainWindow", "Get All Orders"))
        self.actionNew_Order_2.setText(_translate("MainWindow", "New Order"))
        self.actionPay_Supplier.setText(_translate("MainWindow", "Pay Supplier"))
        self.actionFind_Supplier.setText(_translate("MainWindow", "Find Supplier"))
        self.actionUpdate_details.setText(_translate("MainWindow", "Update details"))
        self.actionAll_Orderd.setText(_translate("MainWindow", "All Orders"))
        self.actionFind_Order_2.setText(_translate("MainWindow", "Find Order"))
        self.actionInventory.setText(_translate("MainWindow", "Inventory"))
        self.actionAdd_Category.setText(_translate("MainWindow", "Add Category"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionCheck_Details.setText(_translate("MainWindow", "Check Details"))
        self.actionUpdate_Details.setText(_translate("MainWindow", "Update Details"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())