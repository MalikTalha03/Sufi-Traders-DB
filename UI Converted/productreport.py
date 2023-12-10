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
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(350, 50, 89, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(500, 50, 89, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(650, 50, 89, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 50, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 100, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 130, 781, 411))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 100, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.comboBox_2.hide()
        self.label_3.hide()
        self.comboBoxData()
        self.radioButton.clicked.connect(self.radio1Clicked)
        self.radioButton_2.clicked.connect(self.radio2Clicked)
        self.radioButton_3.clicked.connect(self.radio3Clicked)

        self.comboBox_3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 100, 101, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.comboBox_3.hide()
        self.label_4.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Product Sales Report"))
        self.label.setText(_translate("MainWindow", "Product Sales Report "))
        self.radioButton.setText(_translate("MainWindow", "Monthly"))
        self.radioButton_2.setText(_translate("MainWindow", "Daily"))
        self.radioButton_3.setText(_translate("MainWindow", "Yearly"))
        self.label_2.setText(_translate("MainWindow", "Product"))
        self.label_3.setText(_translate("MainWindow", "Month"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Month"))

    def comboBoxData(self):
        products = self.db.execute_read_query("SELECT productName FROM Products")
        if products is not None:
            for product in products:
                self.comboBox.addItem(product[0])

    def radio1Clicked(self):
        if self.radioButton.isChecked():
            months = ['January','February','March','April','May','June','July','August','September','October','November','December']
            self.comboBox_2.clear()
            for month in months:
                self.comboBox_2.addItem(month)
            years = list(range(2000,2031))
            self.comboBox_3.clear()
            for year in years:
                self.comboBox_3.addItem(str(year))
            self.comboBox_3.show()
            self.label_4.show()
            self.label_4.setText("Year")
            self.comboBox_2.show()
            self.label_3.show()
            self.label_3.setText("Month")
            self.pushButton.setEnabled(True)
            self.pushButton.clicked.connect(self.search)

    def radio2Clicked(self):
        if self.radioButton_2.isChecked():
            self.label_3.show()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            months = ['January','February','March','April','May','June','July','August','September','October','November','December']
            for month in months:
                self.comboBox_3.addItem(month)
            self.comboBox_3.show()
            days = list(range(1,32))
            for day in days:
                self.comboBox_2.addItem(str(day))
            self.comboBox_2.show()
            self.label_3.setText("Day")
            self.label_4.show()
            self.label_4.setText("Month")
            self.pushButton.setEnabled(True)
            self.pushButton.clicked.connect(self.search)

    def radio3Clicked(self):
        if self.radioButton_3.isChecked():
            self.comboBox_3.hide()
            self.label_4.hide()
            years = list(range(2000,2031))
            self.comboBox_2.clear()
            for year in years:
                self.comboBox_2.addItem(str(year))
            self.comboBox_2.show()
            self.label_3.show()
            self.label_3.setText("Year")
            self.pushButton.setEnabled(True)
            self.pushButton.clicked.connect(self.search)

    def search(self):
        if self.radioButton.isChecked():
            self.plot_monthly()
        elif self.radioButton_2.isChecked():
            self.plot_daily()
        elif self.radioButton_3.isChecked():
            self.plot_yearly()
    
    def plot_monthly(self):
        product = self.comboBox.currentText()
        month = self.comboBox_2.currentText()
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        monthno = months.index(month) + 1
        year = self.comboBox_3.currentText()
        rows = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate LIKE '%{monthno}%' AND orderDate LIKE '%{year}%'")
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
        ax.set_ylabel('Sales')
        ax.set_title(f'{product} Sales for {month}')
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        canvas.draw()
        fig.savefig('monthly.png')
        canvas.setParent(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.clicked.connect(self.clear)
    
    def plot_daily(self):
        product = self.comboBox.currentText()
        day = self.comboBox_2.currentText()
        month = self.comboBox_3.currentText()
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        monthno = months.index(month) + 1
        rows = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate LIKE '%{day}%' AND orderDate LIKE '%{monthno}%'")
        total_sales_per_hour = {hour: 0 for hour in range(0, 24)}
        if rows:
            for row in rows:
                rows2 = self.db.execute_read_query("SELECT * FROM Customer_Order_Details WHERE orderID = '{}'".format(row[0]))
                if rows2:
                    for row2 in rows2:
                        order_date = datetime.strptime(row[3], '%Y-%m-%d')
                        total_sales_per_hour[order_date.hour] += float(row2[2]) * float(row2[3])
        else:
            total_sales_per_hour = {hour: 0 for hour in range(0, 24)}
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(list(total_sales_per_hour.keys()), list(total_sales_per_hour.values()))
        ax.set_xlabel('Hour of the Day')
        ax.set_ylabel('Sales')
        ax.set_title(f'{product} Sales for {day}')
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        canvas.draw()
        canvas.setParent(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.clicked.connect(self.clear)

    def plot_yearly(self):
        product = self.comboBox.currentText()
        year = self.comboBox_2.currentText()
        rows = self.db.execute_read_query(f"SELECT * FROM Customer_Order WHERE orderDate LIKE '%{year}%'")
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
        ax.set_ylabel('Sales')
        ax.set_title(f'{product} Sales for {year}')
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        canvas.draw()
        canvas.setParent(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.clicked.connect(self.clear)

    def clear(self):
        self.pushButton_2.setEnabled(False)
        self.comboBox_2.hide()
        self.label_3.hide()
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.pushButton.setEnabled(False)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 110, 741, 391))
        self.widget.setObjectName("widget")
        self.setupUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
