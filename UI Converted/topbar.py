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

        self.menuReports = QtWidgets.QMenu(self)
        self.menuReports.setObjectName("menuReports")
        self.menuReports.setTitle("Reports")

        self.menulogout = QtWidgets.QMenu(self)
        self.menulogout.setObjectName("menulogout")
        self.menulogout.setTitle("Logout")

        self.setupActions()

    def setupActions(self):
        # Customer menu actions
        self.actionNew_Order = QtGui.QAction(self)
        self.actionNew_Order.setObjectName("actionNew_Order")
        self.actionNew_Order.setText("New Order")
        self.actionNew_Order.triggered.connect(self.new_order)

        self.actionGet_Paid = QtGui.QAction(self)
        self.actionGet_Paid.setObjectName("actionGet_Paid")
        self.actionGet_Paid.setText("Get Paid")
        self.actionGet_Paid.triggered.connect(self.custpaid)

        self.actionFind_Order = QtGui.QAction(self)
        self.actionFind_Order.setObjectName("actionFind_Order")
        self.actionFind_Order.setText("Find Order")
        self.actionFind_Order.triggered.connect(self.custorder)

        self.actionUpdate_Customer = QtGui.QAction(self)
        self.actionUpdate_Customer.setObjectName("actionUpdate_Customer")
        self.actionUpdate_Customer.setText("Update Customer")
        self.actionUpdate_Customer.triggered.connect(self.updcust)

        self.actionGet_All_Orders = QtGui.QAction(self)
        self.actionGet_All_Orders.setObjectName("actionGet_All_Orders")
        self.actionGet_All_Orders.setText("Get All Orders")
        self.actionGet_All_Orders.triggered.connect(self.allcustorders)

        self.actionRefundOrder = QtGui.QAction(self)
        self.actionRefundOrder.setObjectName("actionRefundOrder")
        self.actionRefundOrder.setText("Refund Order")
        self.actionRefundOrder.triggered.connect(self.refundorder)

        # Supplier menu actions
        self.actionNew_Order_2 = QtGui.QAction(self)
        self.actionNew_Order_2.setObjectName("actionNew_Order_2")
        self.actionNew_Order_2.setText("New Order")
        self.actionNew_Order_2.triggered.connect(self.suppnew_order)

        self.actionPay_Supplier = QtGui.QAction(self)
        self.actionPay_Supplier.setObjectName("actionPay_Supplier")
        self.actionPay_Supplier.setText("Pay Supplier")
        self.actionPay_Supplier.triggered.connect(self.paysupp)

        self.actionFind_Supplier = QtGui.QAction(self)
        self.actionFind_Supplier.setObjectName("actionFind_Supplier")
        self.actionFind_Supplier.setText("Find Supplier")
        self.actionFind_Supplier.triggered.connect(self.findsupp)

        self.actionUpdate_details = QtGui.QAction(self)
        self.actionUpdate_details.setObjectName("actionUpdate_details")
        self.actionUpdate_details.setText("Update details")
        self.actionUpdate_details.triggered.connect(self.updsupp)

        self.actionAll_Orderd = QtGui.QAction(self)
        self.actionAll_Orderd.setObjectName("actionAll_Orderd")
        self.actionAll_Orderd.setText("All Orders")
        self.actionAll_Orderd.triggered.connect(self.allsupporders)

        self.actionFind_Order_2 = QtGui.QAction(self)
        self.actionFind_Order_2.setObjectName("actionFind_Order_2")
        self.actionFind_Order_2.setText("Find Order")
        self.actionFind_Order_2.triggered.connect(self.findsupporder)

        # Product menu actions
        self.actionInventory = QtGui.QAction(self)
        self.actionInventory.setObjectName("actionInventory")
        self.actionInventory.setText("Inventory")
        self.actionInventory.triggered.connect(self.inv)

        self.actionAdd_Category = QtGui.QAction(self)
        self.actionAdd_Category.setObjectName("actionAdd_Category")
        self.actionAdd_Category.setText("Add Category")
        self.actionAdd_Category.triggered.connect(self.addcategory)

        # Employee menu actions
        self.actionAdd = QtGui.QAction(self)
        self.actionAdd.setObjectName("actionAdd")
        self.actionAdd.setText("Add")
        self.actionAdd.triggered.connect(self.addemp)

        self.actionCheck_Details = QtGui.QAction(self)
        self.actionCheck_Details.setObjectName("actionCheck_Details")
        self.actionCheck_Details.setText("Check Details")
        self.actionCheck_Details.triggered.connect(self.checkempdetails)

        self.actionUpdate_Details = QtGui.QAction(self)
        self.actionUpdate_Details.setObjectName("actionUpdate_Details")
        self.actionUpdate_Details.setText("Update Details")
        self.actionUpdate_Details.triggered.connect(self.updemp)

        self.actionDelete = QtGui.QAction(self)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.setText("Delete")
        self.actionDelete.triggered.connect(self.delemp)

        # Reports menu actions
        self.actionTopSelling = QtGui.QAction(self)
        self.actionTopSelling.setObjectName("actionTopSelling")
        self.actionTopSelling.setText("Top Selling")
        self.actionTopSelling.triggered.connect(self.topSelling)

        self.actionSales = QtGui.QAction(self)
        self.actionSales.setObjectName("actionSales")
        self.actionSales.setText("Sales")
        self.actionSales.triggered.connect(self.sales)

        self.actionProductSales = QtGui.QAction(self)
        self.actionProductSales.setObjectName("actionProductSales")
        self.actionProductSales.setText("Product Sales")
        self.actionProductSales.triggered.connect(self.prodsale)

        self.actionCustomReports = QtGui.QAction(self)
        self.actionCustomReports.setObjectName("actionCustomReports")
        self.actionCustomReports.setText("Custom Reports")
        self.actionCustomReports.triggered.connect(self.customReports)

        # Logout menu actions
        self.actionLogout = QtGui.QAction(self)
        self.actionLogout.setObjectName("actionLogout")
        self.actionLogout.setText("Logout")
        self.actionLogout.triggered.connect(self.logout)

        self.menuCustomer.addAction(self.actionNew_Order)
        self.menuCustomer.addAction(self.actionGet_Paid)
        self.menuCustomer.addAction(self.actionFind_Order)
        self.menuCustomer.addAction(self.actionUpdate_Customer)
        self.menuCustomer.addAction(self.actionGet_All_Orders)
        self.menuCustomer.addAction(self.actionRefundOrder)

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

        self.menuReports.addAction(self.actionTopSelling)
        self.menuReports.addAction(self.actionSales)
        self.menuReports.addAction(self.actionProductSales)
        self.menuReports.addAction(self.actionCustomReports)

        self.menulogout.addAction(self.actionLogout)

        self.addMenu(self.menuCustomer)
        self.addMenu(self.menuSupplier)
        self.addMenu(self.menuProduct)
        self.addMenu(self.menuEmployee)
        self.addMenu(self.menuReports)
        self.addMenu(self.menulogout)

    def new_order(self):
        from form import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def custpaid(self):
        from paymentcust import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def custorder(self):
        from findcustorder import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def updcust(self):
        from updatecustomer import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def allcustorders(self):
        from allcustorders import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def suppnew_order(self):
        from supplierOrder import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def paysupp(self):
        from paysupplier import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def findsupp(self):
        from findsupplier import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def updsupp(self):
        from updsupplier import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def allsupporders(self):
        from allsupporder import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def findsupporder(self):
        from supporderdetail import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def inv(self):
        from checkinventory import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def addcategory(self):
        from addcatedory import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def addemp(self):
        from addemployee import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def checkempdetails(self):
        from empdetail import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def updemp(self):
        from updateemployee import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def delemp(self):
        pass

    def refundorder(self):
        from returns import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def topSelling(self):
        from topselling import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def sales(self):
        from Reports import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def prodsale(self):
        from productreport import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()
    
    def logout(self):
        from db import DatabaseManager
        from datetime import datetime
        self.db = DatabaseManager()
        curr_logged_in = self.db.execute_read_query("SELECT * FROM Employee_Session WHERE currStatus = 'Active'")
        if curr_logged_in:
            for row in curr_logged_in:
                self.db.execute_query("UPDATE Employee_Session SET currStatus = 'Inactive', logoutTime = '{}' WHERE sessionID = '{}'".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), row[0]))
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Logged out Successfully")
            msg.exec()            
        from Login import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()
        self.parent().close()

    def customReports(self):
        from reportsdashboard import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show() 


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    menubar = MenuBar(window)
    window.setMenuBar(menubar)
    window.show()
    app.exec()
