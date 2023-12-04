from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime, timedelta

class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 50, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(410, 50, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 110, 741, 391))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(600, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 510, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 510, 111, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.clear)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sales Report"))
        self.label_2.setText(_translate("MainWindow", "Start Date"))
        self.label_3.setText(_translate("MainWindow", "End Date"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))

    def search(self):
        start_date = self.dateEdit.date().toPyDate()
        end_date = self.dateEdit_2.date().toPyDate()
        sales = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate BETWEEN '{start_date}' AND '{end_date}'")
        total = 0
        if sales:
            for sale in sales:
                orders = self.db.execute_read_query(f"SELECT * FROM Customer_Order_Details WHERE orderID = {sale[0]}")
                for order in orders:
                    total += order[2] * order[3]
        else:
            total = 0
        self.lineEdit.setText(str(total))
        self.plot(start_date, end_date)

    def plot(self, start_date, end_date):
        if (end_date - start_date).days < 31:
            self.plot_monthly(start_date, end_date)
        elif (end_date - start_date).days < 367:
            self.plot_yearly(start_date, end_date)
        else:
            self.plot_all(start_date, end_date)

    def plot_monthly(self, start_date, end_date):
        rows = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate BETWEEN '{start_date}' AND '{end_date}'")
        current_date = datetime.now()
        last_day_of_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        total_sales_per_day = {day: 0 for day in range(1, last_day_of_month.day + 1)}
        if rows:
            for row in rows:
                rows2 = self.db.execute_read_query("SELECT * FROM Customer_Order_Details WHERE orderID = '{}'".format(row[0]))
                if rows2:
                    for row2 in rows2:
                        order_date = datetime.strptime(row[3], '%Y-%m-%d')
                        total_sales_per_day[order_date.day] += float(row2[2]) * float(row2[3])
        else:
            total_sales_per_day = {day: 0 for day in range(1, last_day_of_month.day + 1)}
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(list(total_sales_per_day.keys()), list(total_sales_per_day.values()))
        ax.set_xlabel('Day of the Month')
        ax.set_ylabel('Total Sales')
        ax.set_title('Total Sales for Each Day in Current Month')
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        canvas.draw()

    def plot_yearly(self, start_date, end_date):
        rows = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate BETWEEN '{start_date}' AND '{end_date}'")
        total_sales_per_month = {month: 0 for month in range(1, 13)}
        if rows:
            for row in rows:
                rows2 = self.db.execute_read_query("SELECT * FROM Customer_Order_Details WHERE orderID = '{}'".format(row[0]))
                if rows2:
                    for row2 in rows2:
                        order_date = datetime.strptime(row[3], '%Y-%m-%d')
                        total_sales_per_month[order_date.month] += float(row2[2]) * float(row2[3])
        else:
            total_sales_per_month = {month: 0 for month in range(1, 13)}
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(list(total_sales_per_month.keys()), list(total_sales_per_month.values()))
        ax.set_xlabel('Month of the Year')
        ax.set_ylabel('Total Sales')
        ax.set_title('Total Sales for Each Month in Current Year')
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        canvas.draw()

    def plot_all(self, start_date, end_date):
        rows = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate BETWEEN '{start_date}' AND '{end_date}'")
        total_sales_per_year = {year: 0 for year in range(start_date.year, end_date.year + 1)}
        if rows:
            for row in rows:
                rows2 = self.db.execute_read_query("SELECT * FROM Customer_Order_Details WHERE orderID = '{}'".format(row[0]))
                if rows2:
                    for row2 in rows2:
                        order_date = datetime.strptime(row[3], '%Y-%m-%d')
                        total_sales_per_year[order_date.year] += float(row2[2]) * float(row2[3])
        else:
            total_sales_per_year = {year: 0 for year in range(start_date.year, end_date.year + 1)}
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(list(total_sales_per_year.keys()), list(total_sales_per_year.values()))
        ax.set_xlabel('Year')
        ax.set_ylabel('Total Sales')
        ax.set_title('Total Sales for Each Year in Given Range')
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        canvas.draw()

    def clear(self):
        # remove wigdget to again display graph etx in widget
        #error  QLayout: Attempting to add QLayout "" to QWidget "widget", which already has a layout
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 110, 741, 391))
        self.widget.setObjectName("widget")
        self.lineEdit.setText("")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.setupUi(MainWindow)

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
