from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(210, 20, 89, 20))
        self.radioButton.setObjectName("radioButton")
        self.type = QtWidgets.QButtonGroup(MainWindow)
        self.type.setObjectName("type")
        self.type.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 20, 89, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.type.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(470, 20, 89, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.type.addButton(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(620, 20, 89, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.type.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(490, 80, 131, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.salessub = QtWidgets.QButtonGroup(MainWindow)
        self.salessub.setObjectName("salessub")
        self.salessub.addButton(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(340, 80, 131, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.salessub.addButton(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(180, 80, 141, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.salessub.addButton(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(650, 80, 131, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.salessub.addButton(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(30, 80, 121, 20))
        self.radioButton_9.setObjectName("radioButton_9")
        self.salessub.addButton(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(160, 140, 89, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.datebtn = QtWidgets.QButtonGroup(MainWindow)
        self.datebtn.setObjectName("datebtn")
        self.datebtn.addButton(self.radioButton_10)
        self.radioButton_12 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(280, 140, 89, 20))
        self.radioButton_12.setObjectName("radioButton_12")
        self.datebtn.addButton(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(420, 140, 89, 20))
        self.radioButton_13.setObjectName("radioButton_13")
        self.datebtn.addButton(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_14.setGeometry(QtCore.QRect(30, 140, 89, 20))
        self.radioButton_14.setObjectName("radioButton_14")
        self.datebtn.addButton(self.radioButton_14)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(540, 140, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(680, 140, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 140, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_15 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_15.setGeometry(QtCore.QRect(210, 360, 89, 20))
        self.radioButton_15.setObjectName("radioButton_15")
        self.charts = QtWidgets.QButtonGroup(MainWindow)
        self.charts.setObjectName("charts")
        self.charts.addButton(self.radioButton_15)
        self.radioButton_11 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(380, 360, 89, 20))
        self.radioButton_11.setObjectName("radioButton_11")
        self.charts.addButton(self.radioButton_11)
        self.radioButton_17 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_17.setGeometry(QtCore.QRect(530, 360, 89, 20))
        self.radioButton_17.setObjectName("radioButton_17")
        self.charts.addButton(self.radioButton_17)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 500, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 500, 111, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 500, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 220, 111, 22))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hide()
        self.radioButton.clicked.connect(self.sales)
        self.radioButton_2.clicked.connect(self.finance)
        self.radioButton_3.clicked.connect(self.customer)
        self.radioButton_4.clicked.connect(self.inventory)
        self.radioButton_5.clicked.connect(self.byCustomer)
        self.radioButton_6.clicked.connect(self.byProduct)
        self.radioButton_7.clicked.connect(self.byEmployee)
        self.radioButton_8.clicked.connect(self.byCategory)
        self.radioButton_9.clicked.connect(self.totalSales)
        self.radioButton_13.clicked.connect(self.range)
        self.radioButton_14.clicked.connect(self.today)
        self.radioButton_12.clicked.connect(self.year)
        self.radioButton_10.clicked.connect(self.month)
        self.pushButton_2.clicked.connect(self.radiodata)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Report Type"))
        self.radioButton.setText(_translate("MainWindow", "Sales"))
        self.radioButton_2.setText(_translate("MainWindow", "Financial"))
        self.radioButton_3.setText(_translate("MainWindow", "Customer"))
        self.radioButton_4.setText(_translate("MainWindow", "Inventory"))
        self.radioButton_5.setText(_translate("MainWindow", "By Customer"))
        self.radioButton_6.setText(_translate("MainWindow", "By Product"))
        self.radioButton_7.setText(_translate("MainWindow", "By Employee"))
        self.radioButton_8.setText(_translate("MainWindow", "By Category"))
        self.radioButton_9.setText(_translate("MainWindow", "Total Sales"))
        self.radioButton_10.setText(_translate("MainWindow", "This Month"))
        self.radioButton_12.setText(_translate("MainWindow", "This Year"))
        self.radioButton_13.setText(_translate("MainWindow", "Date Range"))
        self.radioButton_14.setText(_translate("MainWindow", "Today"))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.radioButton_15.setText(_translate("MainWindow", "Bar Chart"))
        self.radioButton_11.setText(_translate("MainWindow", "Pie Chart"))
        self.radioButton_17.setText(_translate("MainWindow", "Line Chart"))
        self.label_3.setText(_translate("MainWindow", "Report Visuals"))
        self.pushButton.setText(_translate("MainWindow", "Download as PDF"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Employee Name"))

    def hide(self):
        self.radioButton_5.hide()
        self.radioButton_6.hide()
        self.radioButton_7.hide()
        self.radioButton_8.hide()
        self.radioButton_9.hide()
        self.radioButton_10.hide()
        self.radioButton_12.hide()
        self.radioButton_13.hide()
        self.radioButton_14.hide()
        self.dateEdit.hide()
        self.dateEdit_2.hide()
        self.label_2.hide()
        self.radioButton_15.hide()
        self.radioButton_11.hide()
        self.radioButton_17.hide()
        self.label_3.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.comboBox.hide()
        self.label_4.hide()
    
    def sales(self):
        self.radioButton_5.setText("By Customer")
        self.radioButton_6.setText("By Product")
        self.radioButton_7.setText("By Employee")
        self.radioButton_8.setText("By Category")
        self.radioButton_9.setText("Total Sales")
        self.showsub()
        self.hidesub()

    def byCustomer(self):
        if self.radioButton_5.text() == "By Customer":
            self.showdatebox()
            self.comboBox.show()
            self.comboBox.clear()
            custs = self.db.execute_read_query("SELECT custFName,custLName FROM Customers")
            for cust in custs:
                self.comboBox.addItem(cust[0] + " " + cust[1])
            self.label_4.show()
            self.label_4.setText("Customer Name")
        elif self.radioButton_5.text() == "Revenue":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_5.text() == "Total Customers":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_5.text() == "All":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
    
    def byProduct(self):
        if self.radioButton_6.text() == "By Product":
            self.showdatebox()
            self.comboBox.show()
            self.comboBox.clear()
            self.comboBox.addItem("All Products")
            self.label_4.show()
            self.label_4.setText("Product Name")
            prods = self.db.execute_read_query("SELECT productName FROM Products")
            for prod in prods:
                self.comboBox.addItem(prod[0])
        elif self.radioButton_6.text() == "Expense":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_6.text() == "New Customers":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_6.text() == "Product Categories":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()

    def byEmployee(self):
        if self.radioButton_7.text() == "By Employee":
            self.showdatebox()
            self.comboBox.show()
            self.comboBox.clear()
            self.comboBox.addItem("All Employees")
            self.label_4.show()
            self.label_4.setText("Employee Name")
            emps = self.db.execute_read_query("SELECT empFName,empLName FROM Employee")
            for emp in emps:
                self.comboBox.addItem(emp[0] + " " + emp[1])
        elif self.radioButton_7.text() == "Profit":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_7.text() == "Returning Customers":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_7.text() == "Product Availability":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
    
    def byCategory(self):
        if self.radioButton_8.text() == "By Category":
            self.showdatebox()
            self.comboBox.show()
            self.comboBox.clear()
            self.comboBox.addItem("All Categories")
            self.label_4.show()
            self.label_4.setText("Category Name")
            cats = self.db.execute_read_query("SELECT categoryName FROM Categories")
            for cat in cats:
                self.comboBox.addItem(cat[0])
        elif self.radioButton_8.text() == "Net Income":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_8.text() == "Customer Loyalty":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_8.text() == "Low Stock Alert":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()

    def totalSales(self):
        if self.radioButton_9.text() == "Total Sales":
            self.radioButton_14.setText("Today")
            self.radioButton_10.setText("This Month")
            self.radioButton_12.setText("This Year")
            self.radioButton_13.setText("Date Range")
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_9.text() == "Cash Flow":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()
        elif self.radioButton_9.text() == "Product Turnover":
            self.showdatebox()
            self.comboBox.clear()
            self.comboBox.hide()
            self.label_4.hide()


    def finance(self):
        self.radioButton_5.setText("Revenue")
        self.radioButton_7.setText("Profit")
        self.radioButton_8.setText("Net Income")
        self.radioButton_9.setText("Cash Flow")
        self.showsub() 
        self.hidesub()
        self.radioButton_6.hide()

    
    def customer(self):
        self.radioButton_5.setText("Total Customers")
        self.radioButton_6.setText("New Customers")
        self.radioButton_7.setText("Returning Customers")
        self.radioButton_8.setText("Customer Loyalty")
        self.radioButton_9.setText("Customer Satisfaction")
        self.showsub() 
        self.hidesub()
        self.radioButton_9.hide()

    def inventory(self):
        self.radioButton_5.setText("All Products")
        self.radioButton_6.setText("Product Categories")
        self.radioButton_7.setText("Product Availability")
        self.radioButton_8.setText("Low Stock Alert")
        self.radioButton_9.setText("Inventory Turnover")
        self.showsub() 
        self.hidesub()

    def showsub(self):
        self.radioButton_5.show()
        self.radioButton_6.show()
        self.radioButton_7.show()
        self.radioButton_8.show()
        self.radioButton_9.show()    

    def hidesub(self):
        self.radioButton_10.hide()
        self.radioButton_12.hide()
        self.radioButton_13.hide()
        self.radioButton_14.hide()
        self.dateEdit.hide()
        self.dateEdit_2.hide()
        self.label_2.hide()
        self.label_4.hide()
        self.comboBox.hide()

    def range(self):
        self.dateEdit.show()
        self.dateEdit_2.show()
        self.label_2.show()
        self.openrep()

    def openrep(self):
        self.label_3.show()
        self.radioButton_15.show()
        self.radioButton_11.show()
        self.radioButton_17.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        if self.radioButton_6.text() == "By Product" and self.comboBox.currentText() == "All Products":
            self.radioButton_11.hide()

    def clearsub(self):
        self.dateEdit.hide()
        self.dateEdit_2.hide()
        self.label_2.hide()

    def today(self):
        self.openrep()
        self.clearsub()

    def month(self):
        self.openrep()
        self.clearsub()

    def year(self):
        self.openrep()
        self.clearsub()

    def showdatebox(self):
        self.radioButton_10.show()
        self.radioButton_12.show()
        self.radioButton_13.show()
        self.radioButton_14.show()

    def radiodata(self):
        query = ""
        specsignal = False
        data = []
        names=[]
        ids=[]
        markings = []
        plotdata = defaultdict(list)
        pltdata = defaultdict(list)
        hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,
                15,16,17,18,19,20,21,22,23,24,25,26,
                27,28,29,30,31]
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        if self.radioButton.isChecked():
            if self.radioButton_9.isChecked() and self.radioButton_9.text() == "Total Sales":
                if self.radioButton_14.isChecked():
                    query = """SELECT
                                    DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                    SUM(COD.quantity * COD.salePrice) AS HourlySales
                                FROM
                                    Customer_Order CO
                                JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CONVERT(DATE, CO.orderDate) = CONVERT(DATE, GETDATE())  
                                GROUP BY
                                    DATEPART(HOUR, CO.orderTime)
                                ORDER BY
                                    OrderHour;
                                """
                    data = self.db.execute_read_query(query)
                    for row in data:
                        hour = row[0]
                        plotdata[hour].append(row[1])
                    for hour in hours:
                        if hour not in plotdata:
                            plotdata[hour].append(0)
                    plotdata = dict(sorted(plotdata.items()))

                elif self.radioButton_10.isChecked():
                    query = """SELECT
                                    DAY(CO.orderDate) AS OrderDay,
                                    SUM(COD.quantity * COD.salePrice) AS DailySales
                                FROM
                                    Customer_Order CO
                                JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    YEAR(CO.orderDate) = YEAR(GETDATE())
                                    AND MONTH(CO.orderDate) = MONTH(GETDATE())
                                GROUP BY
                                    DAY(CO.orderDate)
                                ORDER BY
                                    OrderDay;"""
                    data = self.db.execute_read_query(query)
                    for row in data:
                        day = row[0]
                        plotdata[day].append(row[1])
                    for day in days:
                        if day not in plotdata:
                            plotdata[day].append(0)
                    plotdata = dict(sorted(plotdata.items()))

                elif self.radioButton_12.isChecked():
                    query = """ SELECT
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    SUM(COD.quantity * COD.salePrice) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    YEAR(CO.orderDate) = YEAR(GETDATE())
                                GROUP BY
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderMonth; """
                    data = self.db.execute_read_query(query)
                    for row in data:
                        month = row[0]
                        plotdata[month].append(row[1])
                    for month in months:
                        if month not in plotdata:
                            plotdata[month].append(0)
                    plotdata = dict(sorted(plotdata.items()))

                elif self.radioButton_13.isChecked():
                    query = """SELECT
                                    YEAR(CO.orderDate) AS OrderYear,
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    SUM(COD.quantity * COD.salePrice) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.orderDate BETWEEN '{}' AND '{}'
                                GROUP BY
                                    YEAR(CO.orderDate),
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderYear, OrderMonth;""".format(self.dateEdit.text(), self.dateEdit_2.text())
                    data = self.db.execute_read_query(query)
                    for row in data:
                        plotdata[str(row[1])+"-"+str(int(str(row[0])[-2:]))].append(row[2]) # row[0] is the year, row[1] is the month, row[2] is the sales
                        self.radioButton_17.hide()
            elif self.radioButton_5.isChecked() and self.radioButton_5.text() == "By Customer":
                if self.radioButton_14.isChecked():
                    query = """ SELECT
                                    DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.customerID = '{}'
                                    AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                GROUP BY
                                    DATEPART(HOUR, CO.orderTime)
                                ORDER BY
                                    OrderHour;""".format(self.id())
                    data = self.db.execute_read_query(query)
                    for row in data:
                        plotdata[row[0]].append(row[1])
                    for hour in hours:
                        if hour not in plotdata:
                            plotdata[hour].append(0)
                    plotdata = dict(sorted(plotdata.items()))

                elif self.radioButton_10.isChecked():
                    query = """SELECT
                                    DAY(CO.orderDate) AS OrderDay,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.customerID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                        AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    DAY(CO.orderDate)
                                ORDER BY
                                    OrderDay;""".format(self.id())
                    data = self.db.execute_read_query(query)
                    for row in data:
                        plotdata[row[0]].append(row[1])
                    for day in days:
                        if day not in plotdata:
                            plotdata[day].append(0)
                    plotdata = dict(sorted(plotdata.items()))
                            
                elif self.radioButton_12.isChecked():
                    query = """SELECT
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.customerID = '{}'
                                    AND YEAR(CO.orderDate) = YEAR(GETDATE())
                                GROUP BY
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderMonth;
                                """.format(self.id())
                    data = self.db.execute_read_query(query)
                    for row in data:
                        plotdata[row[0]].append(row[1])
                    for month in months:
                        if month not in plotdata:
                            plotdata[month].append(0)
                    plotdata = dict(sorted(plotdata.items()))

                elif self.radioButton_13.isChecked():
                    query = """SELECT
                                    YEAR(CO.orderDate) AS OrderYear,
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.customerID = '{}'
                                    AND CO.orderDate BETWEEN '{}' AND '{}'
                                GROUP BY
                                    YEAR(CO.orderDate),
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderYear,
                                    OrderMonth;""".format(self.id(),self.dateEdit.text(), self.dateEdit_2.text())
                    data = self.db.execute_read_query(query)
                    for row in data:
                        plotdata[str(row[1])+"-"+str(int(str(row[0])[-2:]))].append(row[2]) # row[0] is the year, row[1] is the month, row[2] is the sales
            elif self.radioButton_6.isChecked() and self.radioButton_6.text() == "By Product":
                if self.comboBox.currentText() == "All Products":
                    print("all products")
                    if self.radioButton_14.isChecked():
                        query = """SELECT DISTINCT
                                        Products.productID,
                                        Products.productName
                                    FROM
                                        Customer_Order CO
                                    JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    JOIN
                                        Products ON COD.productID = Products.productID
                                    WHERE
                                        CONVERT(DATE, CO.orderDate) = GETDATE();"""
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date")
                        for id in ids:
                            query = """SELECT
                                            DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = '{}' AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                        GROUP BY
                                            DATEPART(HOUR, CO.orderTime)
                                        ORDER BY
                                            OrderHour;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[row[0]].append(row[1])
                            for hour in hours:
                                if hour not in plotdata:
                                    plotdata[hour].append(0)
                            plotdata = dict(sorted(plotdata.items()))
                            # add name of id as a single marking
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True

                    elif self.radioButton_10.isChecked():
                        query = """SELECT DISTINCT
                                        Products.productID,
                                        Products.productName
                                    FROM
                                        Customer_Order CO
                                    JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    JOIN
                                        Products ON COD.productID = Products.productID
                                    WHERE
                                        MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                            AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE());"""
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this month")
                        for id in ids:
                            query = """SELECT
                                            DAY(CO.orderDate) AS OrderDay,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                                AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                        GROUP BY
                                            DAY(CO.orderDate)
                                        ORDER BY
                                            OrderDay;""".format(id)
                            
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[row[0]].append(row[1])
                            for day in days:
                                if day not in plotdata.keys():
                                    plotdata[day].append(0)
                            # add name of id as a single marking
                            mrkng = names[ids.index(id)]
                            plotdata = dict(sorted(plotdata.items()))
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True  
                            print(pltdata)
                            print(plotdata)                      
                    elif self.radioButton_12.isChecked():
                        query = """SELECT DISTINCT
                                        Products.productID,
                                        Products.productName
                                    FROM
                                        Customer_Order CO
                                    JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    JOIN
                                        Products ON COD.productID = Products.productID
                                    WHERE
                                        YEAR(CO.orderDate) = YEAR(GETDATE());"""
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this year")
                        for id in ids:
                            query = """SELECT
                                            MONTH(CO.orderDate) AS OrderMonth,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = '{}'
                                            AND YEAR(CO.orderDate) = YEAR(GETDATE())
                                        GROUP BY
                                            MONTH(CO.orderDate)
                                        ORDER BY
                                            OrderMonth;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[row[0]].append(row[1])
                            for month in months:
                                if month not in plotdata:
                                    plotdata[month].append(0)
                            plotdata = dict(sorted(plotdata.items()))
                            # add name of id as a single marking
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True

                    elif self.radioButton_13.isChecked():
                        query = """SELECT DISTINCT
                                        Products.productID,
                                        Products.productName
                                    FROM
                                        Customer_Order CO
                                    JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    JOIN
                                        Products ON COD.productID = Products.productID
                                    WHERE
                                        CO.orderDate BETWEEN '{}' AND '{}';""".format(self.dateEdit.text(), self.dateEdit_2.text())
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date range")
                        for id in ids:
                            query = """SELECT
                                            YEAR(CO.orderDate) AS OrderYear,
                                            MONTH(CO.orderDate) AS OrderMonth,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = '{}'
                                            AND CO.orderDate BETWEEN '{}' AND '{}'
                                        GROUP BY
                                            YEAR(CO.orderDate),
                                            MONTH(CO.orderDate)
                                        ORDER BY
                                            OrderYear,
                                            OrderMonth;""".format(id,self.dateEdit.text(), self.dateEdit_2.text())
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[str(row[1])+"-"+str(int(str(row[0])[-2:]))].append(row[2])
                            # add name of id as a single marking
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True
                else:
                    if self.radioButton_14.isChecked():
                        query = """SELECT
                                        DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                    FROM
                                        Customer_Order CO
                                    LEFT JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    WHERE
                                        COD.productID = '{}'
                                        AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                    GROUP BY
                                        DATEPART(HOUR, CO.orderTime)
                                    ORDER BY
                                        OrderHour;""".format(self.id())
                        data = self.db.execute_read_query(query)
                        for row in data:
                            plotdata[row[0]].append(row[1])
                        for hour in hours:
                            if hour not in plotdata:
                                plotdata[hour].append(0)
                        plotdata = dict(sorted(plotdata.items()))

                    elif self.radioButton_10.isChecked():
                        query = """SELECT
                                        DAY(CO.orderDate) AS OrderDay,
                                        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                    FROM
                                        Customer_Order CO
                                    LEFT JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    WHERE
                                        COD.productID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                            AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                    GROUP BY
                                        DAY(CO.orderDate)
                                    ORDER BY
                                        OrderDay;""".format(self.id())
                        data = self.db.execute_read_query(query)
                        for row in data:
                            plotdata[row[0]].append(row[1])
                        for day in days:
                            if day not in plotdata:
                                plotdata[day].append(0)
                        plotdata = dict(sorted(plotdata.items()))
                                
                    elif self.radioButton_12.isChecked():
                        query = """SELECT
                                        MONTH(CO.orderDate) AS OrderMonth,
                                        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                    FROM
                                        Customer_Order CO
                                    LEFT JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    WHERE
                                        COD.productID = '{}'
                                        AND YEAR(CO.orderDate) = YEAR(GETDATE())
                                    GROUP BY
                                        MONTH(CO.orderDate
                                    ORDER BY
                                        Order
                                    """.format(self.id())
                        data = self.db.execute_read_query(query)
                        for row in data:
                            plotdata[row[0]].append(row[1])
                        for month in months:
                            if month not in plotdata:
                                plotdata[month].append(0)
                        plotdata = dict(sorted(plotdata.items()))

                    elif self.radioButton_13.isChecked():
                        query = """SELECT
                                        YEAR(CO.orderDate) AS OrderYear,
                                        MONTH(CO.orderDate) AS OrderMonth,
                                        ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                    FROM
                                        Customer_Order CO
                                    LEFT JOIN
                                        Customer_Order_Details COD ON CO.orderID = COD.orderID
                                    WHERE
                                        COD.productID = '{}'
                                        AND CO.orderDate BETWEEN '{}' AND '{}'
                                    GROUP BY
                                        YEAR(CO.orderDate),
                                        MONTH(CO.orderDate)
                                    ORDER BY
                                        OrderYear,
                                        OrderMonth;""".format(self.id(),self.dateEdit.text(), self.dateEdit_2.text())
                        data = self.db.execute_read_query(query)
                        for row in data:
                            plotdata[str(row[1])+"-"+str(int(str(row[0])[-2:]))].append(row[2])            
            elif self.radioButton_7.isChecked() and self.radioButton_7.text() == "By Employee":
                if self.comboBox.currentText() == "All Employees":
                    if self.radioButton_14.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                CONVERT(DATE, CO.orderDate) = GETDATE();
                        """
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date")
                        for id in ids:
                            query = """SELECT
                                            DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            CO.employeeID = '{}' AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                        GROUP BY
                                            DATEPART(HOUR, CO.orderTime)
                                        ORDER BY
                                            OrderHour;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for hour in hours:
                                if hour not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            plotdata = dict(sorted(plotdata.items()))
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True

                    elif self.radioButton_10.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                    AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE());"""
                        
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this month")
                        for id in ids:
                            query = """
                                SELECT
                                    DAY(CO.orderDate) AS OrderDay,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.employeeID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                        AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    DAY(CO.orderDate)
                                ORDER BY
                                    OrderDay;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            plotdata = dict(sorted(plotdata.items()))
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True
                    elif self.radioButton_12.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE());"""
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this year")
                        for id in ids:
                            query = """
                                SELECT
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.employeeID = '{}' AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderMonth;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for month in months:
                                if month not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            plotdata = dict(sorted(plotdata.items()))
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True

                    elif self.radioButton_13.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}';""".format(self.dateEdit.text(), self.dateEdit_2.text())
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date range")
                        for id in ids:
                            query = """
                                SELECT
                                    CONVERT(DATE, CO.orderDate) AS OrderDate,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.employeeID = '{}' AND CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}'
                                GROUP BY
                                    CONVERT(DATE, CO.orderDate)
                                ORDER BY
                                    OrderDate;""".format(id, self.dateEdit.text(), self.dateEdit_2.text())
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            plotdata = dict(sorted(plotdata.items()))
                            mrkng = names[ids.index(id)]
                            pltdata[mrkng] = plotdata
                            plotdata = defaultdict(list)
                            specsignal = True
                elif self.comboBox.currentText() != "All Employees":
                    if self.radioButton_14.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                CONVERT(DATE, CO.orderDate) = GETDATE()
                                    AND Employee.empFName = '{}'
                                    AND Employee.empLName = '{}';
                        """.format(self.comboBox.currentText().split()[0], self.comboBox.currentText().split()[1])
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date")
                        for id in ids:
                            query = """SELECT
                                            DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            CO.employeeID = '{}' AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                        GROUP BY
                                            DATEPART(HOUR, CO.orderTime)
                                        ORDER BY
                                            OrderHour;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for hour in hours:
                                if hour not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))

                    elif self.radioButton_10.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                    AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                    AND Employee.empFName = '{}'
                                    AND Employee.empLName = '{}';""".format(self.comboBox.currentText().split()[0], self.comboBox.currentText().split()[1])
                        
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this month")
                        for id in ids:
                            query = """
                                SELECT
                                    DAY(CO.orderDate) AS OrderDay,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.employeeID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                        AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    DAY(CO.orderDate)
                                ORDER BY
                                    OrderDay;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))
                    elif self.radioButton_12.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                    AND Employee.empFName = '{}'
                                    AND Employee.empLName = '{}';""".format(self.comboBox.currentText().split()[0], self.comboBox.currentText().split()[1])
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this year")
                        for id in ids:
                            query = """
                                SELECT
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.employeeID = '{}' AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderMonth;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for month in months:
                                if month not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))
                    elif self.radioButton_13.isChecked():
                        query = """
                            SELECT DISTINCT
                                Employee.employeeID,
                                Employee.empFName,
                                Employee.empLName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Employee ON CO.employeeID = Employee.employeeID
                            WHERE
                                CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}'
                                    AND Employee.empFName = '{}'
                                    AND Employee.empLName = '{}';""".format(self.dateEdit.text(), self.dateEdit_2.text(), self.comboBox.currentText().split()[0], self.comboBox.currentText().split()[1])
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1] + " " + row[2])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date range")
                        for id in ids:
                            query = """
                                SELECT
                                    CONVERT(DATE, CO.orderDate) AS OrderDate,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    CO.employeeID = '{}' AND CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}'
                                GROUP BY
                                    CONVERT(DATE, CO.orderDate)
                                ORDER BY
                                    OrderDate;""".format(id, self.dateEdit.text(), self.dateEdit_2.text())
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))
            elif self.radioButton_8.isChecked() and self.radioButton_8.text() == "By Category":
                if self.comboBox.currentText() == "All Categories":
                    if self.radioButton_14.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            WHERE
                                CONVERT(DATE, CO.orderDate) = GETDATE();
                        """
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date")
                        for id in ids:
                            query = """SELECT
                                            DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = '{}' AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                        GROUP BY
                                            DATEPART(HOUR, CO.orderTime)
                                        ORDER BY
                                            OrderHour;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for hour in hours:
                                if hour not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            


                    elif self.radioButton_10.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            WHERE
                                MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                    AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE());"""
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this month")
                        for id in ids:
                            query = """
                                SELECT
                                    DAY(CO.orderDate) AS OrderDay,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    COD.productID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                        AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    DAY(CO.orderDate)
                                ORDER BY
                                    OrderDay;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))

                    elif self.radioButton_12.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            WHERE
                                YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE());"""
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this year")
                        for id in ids:
                            query = """
                                SELECT
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    COD.productID = '{}' AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderMonth;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for month in months:
                                if month not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))

                    elif self.radioButton_13.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            WHERE
                                CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}';""".format(self.dateEdit.text(), self.dateEdit_2.text())
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date range")
                        for id in ids:
                            query = """
                                SELECT
                                    CONVERT(DATE, CO.orderDate) AS OrderDate,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    COD.productID = '{}' AND CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}'
                                GROUP BY
                                    CONVERT(DATE, CO.orderDate)
                                ORDER BY
                                    OrderDate;""".format(id, self.dateEdit.text(), self.dateEdit_2.text())
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
                            plotdata = dict(sorted(plotdata.items()))

                elif self.comboBox.currentText() != "All Categories":
                    if self.radioButton_14.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            JOIN
                                Product_Category ON Products.categoryID = Product_Category.categoryID
                            WHERE
                                CONVERT(DATE, CO.orderDate) = GETDATE()
                                    AND Product_Category.categoryName = '{}';
                        """.format(self.comboBox.currentText())
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date")
                        for id in ids:
                            query = """SELECT
                                            DATEPART(HOUR, CO.orderTime) AS OrderHour,
                                            ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS HourlySales
                                        FROM
                                            Customer_Order CO
                                        LEFT JOIN
                                            Customer_Order_Details COD ON CO.orderID = COD.orderID
                                        WHERE
                                            COD.productID = '{}' AND CONVERT(DATE, CO.orderDate) = GETDATE()
                                        GROUP BY
                                            DATEPART(HOUR, CO.orderTime)
                                        ORDER BY
                                            OrderHour;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for hour in hours:
                                if hour not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]

                    elif self.radioButton_10.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            JOIN
                                Product_Category ON Products.categoryID = Product_Category.categoryID
                            WHERE
                                MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                    AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                    AND Product_Category.categoryName
                                        = '{}';""".format(self.comboBox.currentText())
                        
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this month")
                        for id in ids:
                            query = """
                                SELECT
                                    DAY(CO.orderDate) AS OrderDay,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    COD.productID = '{}' AND MONTH(CONVERT(DATE, CO.orderDate)) = MONTH(GETDATE())
                                        AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    DAY(CO.orderDate)
                                ORDER BY
                                    OrderDay;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]

                    elif self.radioButton_12.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            JOIN
                                Product_Category ON Products.categoryID = Product_Category.categoryID
                            WHERE
                                YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                    AND Product_Category.categoryName = '{}';""".format(self.comboBox.currentText())
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this year")
                        for id in ids:
                            query = """
                                SELECT
                                    MONTH(CO.orderDate) AS OrderMonth,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS MonthlySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    COD.productID = '{}' AND YEAR(CONVERT(DATE, CO.orderDate)) = YEAR(GETDATE())
                                GROUP BY
                                    MONTH(CO.orderDate)
                                ORDER BY
                                    OrderMonth;""".format(id)
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for month in months:
                                if month not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]

                    elif self.radioButton_13.isChecked():
                        query = """
                            SELECT DISTINCT
                                Products.productID,
                                Products.productName
                            FROM
                                Customer_Order CO
                            JOIN
                                Customer_Order_Details COD ON CO.orderID = COD.orderID
                            JOIN
                                Products ON COD.productID = Products.productID
                            JOIN
                                Product_Category ON Products.categoryID = Product_Category.categoryID
                            WHERE
                                CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}'
                                    AND Product_Category.categoryName = '{}';""".format(self.dateEdit.text(), self.dateEdit_2.text(), self.comboBox.currentText())
                        data = self.db.execute_read_query(query)
                        if data is not None:
                            for row in data:
                                names.append(row[1])
                                ids.append(row[0])
                        else:
                            self.error("No data found for this date range")
                        for id in ids:
                            query = """
                                SELECT
                                    CONVERT(DATE, CO.orderDate) AS OrderDate,
                                    ISNULL(SUM(COD.quantity * COD.salePrice), 0) AS DailySales
                                FROM
                                    Customer_Order CO
                                LEFT JOIN
                                    Customer_Order_Details COD ON CO.orderID = COD.orderID
                                WHERE
                                    COD.productID = '{}' AND CONVERT(DATE, CO.orderDate) BETWEEN '{}' AND '{}'
                                GROUP BY
                                    CONVERT(DATE, CO.orderDate)
                                ORDER BY
                                    OrderDate;""".format(id, self.dateEdit.text(), self.dateEdit_2.text())
                            data = self.db.execute_read_query(query)
                            for row in data:
                                plotdata[names[ids.index(id)]].append(row[1])
                            for day in days:
                                if day not in plotdata[names[ids.index(id)]]:
                                    plotdata[names[ids.index(id)]].append(0)
                            # add names as markings
                            markings = [names[ids.index(id)] for id in ids]
        elif self.radioButton_2.isChecked():
            if self.radioButton_9.isChecked() and self.radioButton_9.text() == "Cash Flow":
                if self.radioButton_14.isChecked():
                    query = "SELECT SUM(totalAmount) FROM Customer_Transactions WHERE transactionDate = GETDATE()"
                elif self.radioButton_10.isChecked():
                    query = "SELECT SUM(totalAmount) FROM Customer_Transactions WHERE MONTH(transactionDate) = MONTH(GETDATE()) AND YEAR(transactionDate) = YEAR(GETDATE())"
                elif self.radioButton_12.isChecked():
                    query = "SELECT SUM(totalAmount) FROM Customer_Transactions WHERE YEAR(transactionDate) = YEAR(GETDATE())"
                elif self.radioButton_13.isChecked():
                    query = "SELECT SUM(totalAmount) FROM Customer_Transactions WHERE transactionDate BETWEEN '" + self.dateEdit.text() + "' AND '" + self.dateEdit_2.text() + "'"

            elif self.radioButton_7.isChecked() and self.radioButton_7.text() == "Profit":
                if self.radioButton_14.isChecked():
                    query = """
                        SELECT SUM(COD.quantity * (COD.salePrice - P.purchasePrice))
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        WHERE CO.orderDate = GETDATE()
                    """
                elif self.radioButton_10.isChecked():
                    query = """
                        SELECT SUM(COD.quantity * (COD.salePrice - P.purchasePrice))
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        WHERE MONTH(CO.orderDate) = MONTH(GETDATE()) AND YEAR(CO.orderDate) = YEAR(GETDATE())
                    """
                elif self.radioButton_12.isChecked():
                    query = """
                        SELECT SUM(COD.quantity * (COD.salePrice - P.purchasePrice))
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        WHERE YEAR(CO.orderDate) = YEAR(GETDATE())
                    """
                elif self.radioButton_13.isChecked():
                    query = """
                        SELECT SUM(COD.quantity * (COD.salePrice - P.purchasePrice))
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        WHERE CO.orderDate BETWEEN '{}' AND '{}'
                    """.format(self.dateEdit.text(), self.dateEdit_2.text())

            elif self.radioButton_8.isChecked() and self.radioButton_8.text() == "Net Income":
                if self.radioButton_14.isChecked():
                    query = """
                        SELECT (SUM(COD.quantity * (COD.salePrice - P.purchasePrice)) - 
                                COALESCE(SUM(D.amount), 0)) AS netIncome
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        LEFT JOIN Discounts D ON CO.orderID = D.orderID
                        WHERE CO.orderDate = GETDATE()
                    """
                elif self.radioButton_10.isChecked():
                    query = """
                        SELECT (SUM(COD.quantity * (COD.salePrice - P.purchasePrice)) - 
                                COALESCE(SUM(D.amount), 0)) AS netIncome
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        LEFT JOIN Discounts D ON CO.orderID = D.orderID
                        WHERE MONTH(CO.orderDate) = MONTH(GETDATE()) AND YEAR(CO.orderDate) = YEAR(GETDATE())
                    """
                elif self.radioButton_12.isChecked():
                    query = """
                        SELECT (SUM(COD.quantity * (COD.salePrice - P.purchasePrice)) - 
                                COALESCE(SUM(D.amount), 0)) AS netIncome
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        LEFT JOIN Discounts D ON CO.orderID = D.orderID
                        WHERE YEAR(CO.orderDate) = YEAR(GETDATE())
                    """
                elif self.radioButton_13.isChecked():
                    query = """
                        SELECT (SUM(COD.quantity * (COD.salePrice - P.purchasePrice)) - 
                                COALESCE(SUM(D.amount), 0)) AS netIncome
                        FROM Customer_Order_Details COD
                        JOIN Products P ON COD.productID = P.productID
                        JOIN Customer_Order CO ON COD.orderID = CO.orderID
                        LEFT JOIN Discounts D ON CO.orderID = D.orderID
                        WHERE CO.orderDate BETWEEN '{}' AND '{}'
                    """.format(self.dateEdit.text(), self.dateEdit_2.text())

        elif self.radioButton_3.isChecked():
            if self.radioButton_5.isChecked() and self.radioButton_5.text() == "Total Customers":
                pass
            elif self.radioButton_6.isChecked() and self.radioButton_6.text() == "New Customers":
                pass
            elif self.radioButton_7.isChecked() and self.radioButton_7.text() == "Returning Customers":
                pass
            elif self.radioButton_8.isChecked() and self.radioButton_8.text() == "Customer Loyalty":
                pass
        elif self.radioButton_4.isChecked():
            if self.radioButton_5.isChecked() and self.radioButton_5.text() == "All Products":
                pass
            elif self.radioButton_6.isChecked() and self.radioButton_6.text() == "Product Categories":
                pass
            elif self.radioButton_7.isChecked() and self.radioButton_7.text() == "Product Availability":
                pass
            elif self.radioButton_8.isChecked() and self.radioButton_8.text() == "Low Stock Alert":
                pass
        if pltdata == {} and plotdata == {}: 
            self.error("No data found for this query")
            return 
        if specsignal:
            self.plotspecial(pltdata)
        else:
            if all(value[0] == 0 for value in plotdata.values()):
                self.error("No data found for this query")
                return
            self.plot(plotdata)
        
    def id(self):
        name = self.comboBox.currentText()
        if self.label_4.text() == "Employee Name":
            fname = name.split()[0]
            lname = name.split()[1]
            query = "SELECT employeeID FROM Employee WHERE empFName = '{}' AND empLName = '{}'".format(fname,lname)
        elif self.label_4.text() == "Customer Name":
            fname = name.split()[0]
            lname = name.split()[1]
            query = "SELECT customerID FROM Customers WHERE custFName = '{}' AND custLName = '{}'".format(fname,lname)
        elif self.label_4.text() == "Product Name":
            query = "SELECT productID FROM Products WHERE productName = '{}'".format(name)
        elif self.label_4.text() == "Category Name":
            query = "SELECT categoryID FROM Product_Category WHERE categoryName = '{}'".format(name)
        id = self.db.execute_read_query(query)
        
        if id is not None:
            return id[0][0]
        else:
            self.error("No ID found for this name")
    
    def plot(self,data):
        if self.radioButton_15.isChecked():
            self.bar(data)
        elif self.radioButton_11.isChecked():
            self.pie(data)
        elif self.radioButton_17.isChecked():
            self.linechart(data)  
    def plotspecial(self,data):
        if self.radioButton_15.isChecked():
            self.barspec(data)
        elif self.radioButton_17.isChecked():
            self.linechartspec(data)
    def bar(self,data):
        x = list(data.keys())
        y = [item[0] for item in data.values()]
        plt.bar(x,y)
        plt.show()

    def pie(self, data):
        import numpy as np
        x = list(data.keys())
        labels = []
        y = []
        if self.radioButton_14.isChecked():
            for i in range(0, len(x), 4):
                label_range = f"{x[i]}-{x[i + 3]}" if i + 3 < len(x) else f"{x[i]}-{x[-1]}"
                labels.append(label_range)
                y_values = [data[key][0] for key in x[i:i + 4]]
                total_sales = sum(y_values)
                y.append(total_sales)
        elif self.radioButton_10.isChecked():
            for i in range(0, len(x), 8):
                label_range = f"{x[i]}-{x[i + 7]}" if i + 7 < len(x) else f"{x[i]}-{x[-1]}"
                labels.append(label_range)
                y_values = [data[key][0] for key in x[i:i + 8]]
                total_sales = sum(y_values)
                y.append(total_sales)
        elif self.radioButton_12.isChecked():
            for i in range(0, len(x), 3):
                label_range = f"{x[i]}-{x[i + 2]}" if i + 2 < len(x) else f"{x[i]}-{x[-1]}"
                labels.append(label_range)
                y_values = [data[key][0] for key in x[i:i + 3]]
                total_sales = sum(y_values)
                y.append(total_sales)
        else:
            for i in range(0, len(x), 4):
                label_range = f"{x[i]}-{x[i + 3]}" if i + 3 < len(x) else f"{x[i]}-{x[-1]}"
                labels.append(label_range)
                y_values = [data[key][0] for key in x[i:i + 4]]
                total_sales = sum(y_values)
                y.append(total_sales)
        colors = plt.cm.Dark2(np.arange(len(labels)))
        wedges, texts, autotexts = plt.pie(y, labels=labels, autopct='%1.1f%%', colors=colors)

        for text, autotext, color in zip(texts, autotexts, colors):
            text.set_color(color)
            autotext.set_color(color)
        plt.legend(labels, loc="upper left", bbox_to_anchor=(1, 1))
        plt.show()

    def linechart(self,data):
        x = list(data.keys())
        y = [item[0] for item in data.values()]
        plt.plot(x,y)
        plt.show()

    def barspec(self,data):
        import numpy as np
        num_names = len(data)
        bar_width = 0.35  
        index = np.arange(len(list(data.values())[0]))  

        for i, (name, sales_data) in enumerate(data.items()):
            hours = list(sales_data.keys())
            sales = [sum(sales_list) for sales_list in sales_data.values()]

            plt.bar(index + i * bar_width, sales, bar_width, label=name)

        plt.xticks(index + bar_width * (num_names - 1) / 2, hours)
        plt.legend()
        plt.show()

    def linechartspec(self,data):
        for name, sales_data in data.items():
            hours = list(sales_data.keys())
            sales = [sum(sales_list) for sales_list in sales_data.values()]

            plt.plot(hours, sales, label=name)

        plt.legend()
        plt.show()
    


    def error(self,message):
        from PyQt6.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
