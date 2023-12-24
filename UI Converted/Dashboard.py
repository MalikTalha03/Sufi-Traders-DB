from PyQt6 import QtCore, QtGui, QtWidgets
from topbar import MenuBar
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from db import DatabaseManager
import calendar

class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()
        self.name = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 80, 751, 421))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(620, 20, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 510, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.emp()
        self.todaysales()
        self.plot()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.label.setText(_translate("MainWindow", "Today Sales"))
        self.label_2.setText(_translate("MainWindow", "Monthly Sales"))
        self.label_3.setText(_translate("MainWindow", "Welcome " + self.name))
    
    def emp(self):
        self.name,id = self.db.curr_loggedin()
        
    def plot(self):
        total_sales_per_day = {day: 0 for day in range(1, calendar.monthrange(datetime.now().year, datetime.now().month)[1] + 1)}
        query = """
            SELECT DAY(Customer_Order.orderDate) AS orderDay, 
                SUM(Customer_Order_Details.quantity * Customer_Order_Details.salePrice) AS totalSales
            FROM Customer_Order
            LEFT JOIN Customer_Order_Details ON Customer_Order.orderID = Customer_Order_Details.orderID
            WHERE MONTH(Customer_Order.orderDate) = MONTH(GETDATE())
            GROUP BY DAY(Customer_Order.orderDate)
        """
        rows = self.db.execute_read_query(query)
        for row in rows:
            total_sales_per_day[row[0]] = float(row[1])
        fig, ax = plt.subplots()
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        ax.plot(total_sales_per_day.keys(), total_sales_per_day.values(), color ='blue' , marker='o', linestyle='solid')
        ax.set_xlabel('Day of the Month')
        ax.set_ylabel('Total Sales')
        ax.set_title('Total Sales for Each Day in Current Month')
        canvas.draw()

    def todaysales(self):
        query = """
            SELECT COALESCE(SUM(Customer_Order_Details.quantity * Customer_Order_Details.salePrice), 0) AS totalSales
            FROM Customer_Order
            LEFT JOIN Customer_Order_Details ON Customer_Order.orderID = Customer_Order_Details.orderID
            WHERE Customer_Order.orderDate = '{}'
        """.format(datetime.today().strftime('%Y-%m-%d'))
        total = self.db.execute_read_query(query)[0][0]
        self.lineEdit.setText(str(total))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
