# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from topbar import MenuBar
import pyodbc
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import calendar
from collections import defaultdict
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


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
        #plotting a graph for monthly sales and showing in widget
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=MALIK-TALHA;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        try:
            with pyodbc.connect(self.cnxn_str) as cnxn:
                cursor = cnxn.cursor()
                cursor.execute("SELECT * FROM Customer_Order WHERE MONTH(orderDate) = MONTH(GETDATE())")
                rows = cursor.fetchall()

                current_date = datetime.now()
                last_day_of_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
                total_sales_per_day = {day: 0 for day in range(1, last_day_of_month.day + 1)}

                if rows:
                    for row in rows:
                        cursor.execute(
                            "SELECT * FROM Customer_Order_Details WHERE orderID = ?", row[0]
                        )
                        rows2 = cursor.fetchall()

                        if rows2:
                            for row2 in rows2:
                                order_date = datetime.strptime(row[3], '%Y-%m-%d')
                                total_sales_per_day[order_date.day] += float(row2[2]) * float(row2[3])

            # Plotting the bar graph
            # Plotting the bar graph
            fig, ax = plt.subplots()
            canvas = FigureCanvas(fig)
            canvas.setGeometry(0, 0, 751, 421)
            layout = QtWidgets.QVBoxLayout(self.widget)
            layout.addWidget(canvas)

            # Plotting the line graph on the canvas
            ax.plot(total_sales_per_day.keys(), total_sales_per_day.values(), color='blue')
            ax.set_xlabel('Day of the Month')
            ax.set_ylabel('Total Sales')
            ax.set_title('Total Sales for Each Day in Current Month')

            # Draw the canvas
            canvas.draw()


                                

        except pyodbc.Error as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(str(e))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.exec()
        finally:
            if cnxn:
                cnxn.close()

    def todaysales(self):
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=MALIK-TALHA;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        total = 0
        try:
            with pyodbc.connect(self.cnxn_str) as cnxn:
                cursor = cnxn.cursor()
                cursor.execute(
                    "SELECT * FROM Customer_Order WHERE orderDate = ?", datetime.today().strftime('%Y-%m-%d')
                )
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        cursor.execute(
                            "SELECT * FROM Customer_Order_Details WHERE orderID = ?", row[0]
                        )
                        rows2 = cursor.fetchall()
                        if rows2:
                            for row2 in rows2:
                                total += (row2[2] * row2[3])
                    self.lineEdit.setText(str(total))
                else:
                    self.lineEdit.setText(str(0))
        except pyodbc.Error as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(str(e))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.exec()
        finally:
            if cnxn:
                cnxn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
