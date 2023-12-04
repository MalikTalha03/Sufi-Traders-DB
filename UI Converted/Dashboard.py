from PyQt6 import QtCore, QtGui, QtWidgets
from topbar import MenuBar
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import calendar
from collections import defaultdict
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from db import DatabaseManager


class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()

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
        self.widget.setGeometry(QtCore.QRect(20, 80, 751, 421))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(230, 20, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 510, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.todaysales()
        self.plot()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Today Sales"))
        self.label_2.setText(_translate("MainWindow", "Monthly Sales"))
    
    def plot(self):
        rows = self.db.execute_read_query("SELECT * FROM Customer_Order WHERE MONTH(orderDate) = MONTH(GETDATE())")
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
        fig, ax = plt.subplots()
        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, 751, 421)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)

        ax.plot(total_sales_per_day.keys(), total_sales_per_day.values(), color='blue')
        ax.set_xlabel('Day of the Month')
        ax.set_ylabel('Total Sales')
        ax.set_title('Total Sales for Each Day in Current Month')
        canvas.draw()

    def todaysales(self):
        
        total = 0
        rows = self.db.execute_read_query("SELECT * FROM Customer_Order WHERE orderDate = '{}'".format(datetime.today().strftime('%Y-%m-%d')))
        if rows:
            for row in rows:
                rows2 = self.db.execute_read_query("SELECT * FROM Customer_Order_Details WHERE orderID = '{}'".format(row[0]))
                if rows2:
                    for row2 in rows2:
                        total += (row2[2] * row2[3])
            self.lineEdit.setText(str(total))
        else:
            self.lineEdit.setText(str(0))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
