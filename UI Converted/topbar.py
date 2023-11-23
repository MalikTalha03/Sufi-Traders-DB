from PyQt6 import QtWidgets, QtGui, QtCore

class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.menuCustomer = QtWidgets.QMenu(self)
        self.menuCustomer.setObjectName("menuCustomer")
        self.menuCustomer.setTitle("Customer")

        self.menuSupplier = QtWidgets.QMenu(self)
        self.menuSupplier.setObjectName("menuSupplier")
        self.menuSupplier.setTitle("Supplier")

        self.menuProduct = QtWidgets.QMenu(self)
        self.menuProduct.setObjectName("menuProduct")
        self.menuProduct.setTitle("Product")

        self.menuEmployee = QtWidgets.QMenu(self)
        self.menuEmployee.setObjectName("menuEmployee")
        self.menuEmployee.setTitle("Employee")

        self.setupActions()

    def setupActions(self):
        # Customer menu actions
        self.actionNew_Order = QtGui.QAction(self)
        self.actionNew_Order.setObjectName("actionNew_Order")
        self.actionNew_Order.setText("New Order")

        self.actionGet_Paid = QtGui.QAction(self)
        self.actionGet_Paid.setObjectName("actionGet_Paid")
        self.actionGet_Paid.setText("Get Paid")

        self.actionFind_Order = QtGui.QAction(self)
        self.actionFind_Order.setObjectName("actionFind_Order")
        self.actionFind_Order.setText("Find Order")

        self.actionUpdate_Customer = QtGui.QAction(self)
        self.actionUpdate_Customer.setObjectName("actionUpdate_Customer")
        self.actionUpdate_Customer.setText("Update Customer")

        self.actionGet_All_Orders = QtGui.QAction(self)
        self.actionGet_All_Orders.setObjectName("actionGet_All_Orders")
        self.actionGet_All_Orders.setText("Get All Orders")

        # Supplier menu actions
        self.actionNew_Order_2 = QtGui.QAction(self)
        self.actionNew_Order_2.setObjectName("actionNew_Order_2")
        self.actionNew_Order_2.setText("New Order")

        self.actionPay_Supplier = QtGui.QAction(self)
        self.actionPay_Supplier.setObjectName("actionPay_Supplier")
        self.actionPay_Supplier.setText("Pay Supplier")

        self.actionFind_Supplier = QtGui.QAction(self)
        self.actionFind_Supplier.setObjectName("actionFind_Supplier")
        self.actionFind_Supplier.setText("Find Supplier")

        self.actionUpdate_details = QtGui.QAction(self)
        self.actionUpdate_details.setObjectName("actionUpdate_details")
        self.actionUpdate_details.setText("Update details")

        self.actionAll_Orderd = QtGui.QAction(self)
        self.actionAll_Orderd.setObjectName("actionAll_Orderd")
        self.actionAll_Orderd.setText("All Orders")

        self.actionFind_Order_2 = QtGui.QAction(self)
        self.actionFind_Order_2.setObjectName("actionFind_Order_2")
        self.actionFind_Order_2.setText("Find Order")

        # Product menu actions
        self.actionInventory = QtGui.QAction(self)
        self.actionInventory.setObjectName("actionInventory")
        self.actionInventory.setText("Inventory")

        self.actionAdd_Category = QtGui.QAction(self)
        self.actionAdd_Category.setObjectName("actionAdd_Category")
        self.actionAdd_Category.setText("Add Category")

        # Employee menu actions
        self.actionAdd = QtGui.QAction(self)
        self.actionAdd.setObjectName("actionAdd")
        self.actionAdd.setText("Add")

        self.actionCheck_Details = QtGui.QAction(self)
        self.actionCheck_Details.setObjectName("actionCheck_Details")
        self.actionCheck_Details.setText("Check Details")

        self.actionUpdate_Details = QtGui.QAction(self)
        self.actionUpdate_Details.setObjectName("actionUpdate_Details")
        self.actionUpdate_Details.setText("Update Details")

        self.actionDelete = QtGui.QAction(self)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.setText("Delete")

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

        self.addMenu(self.menuCustomer)
        self.addMenu(self.menuSupplier)
        self.addMenu(self.menuProduct)
        self.addMenu(self.menuEmployee)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    menubar = MenuBar(window)
    window.setMenuBar(menubar)

    # Add other UI elements...

    window.show()
    app.exec()
