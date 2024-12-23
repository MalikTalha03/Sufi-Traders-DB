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
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 771, 471))
        self.widget.setObjectName("widget")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 20, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(450, 20, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 20, 71, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 20, 71, 24))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Top Selling Products"))
        self.label.setText(_translate("MainWindow", "Start Date"))
        self.label_2.setText(_translate("MainWindow", "End Date"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
    
    def search(self):
        start_date = self.dateEdit.date().toString("yyyy-MM-dd")
        end_date = self.dateEdit_2.date().toString("yyyy-MM-dd")
        result = self.db.execute_read_query(
            "SELECT orderID FROM Customer_Order WHERE orderDate BETWEEN '{}' AND '{}'".format(start_date, end_date)
        )
        prod = {}
        if result:
            for res in result:
                order_id = res[0]
                result2 = self.db.execute_read_query("""
                    SELECT c.productID, c.quantity, p.productName
                    FROM Customer_Order_Details c
                    JOIN Products p ON c.productID = p.productID
                    WHERE c.orderID = '{}'
                """.format(order_id))
                for res2 in result2:
                    prod_id, quantity, prod_name = res2[0], res2[1], res2[2]
                    prod[prod_name] = prod.get(prod_name, 0) + quantity
        top = sorted(prod.items(), key=lambda x: x[1], reverse=True)[:5]
        if len(top) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("No data found!")
            msg.setWindowTitle("Warning")
            msg.exec()
            return
        labels, sizes = zip(*top)
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('None')
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')
        canvas = FigureCanvas(fig)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(canvas)
        self.widget.setStyleSheet("background-color: transparent;")
        self.widget.show()

    def clear(self):
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 771, 471))
        self.widget.setObjectName("widget")
        self.widget.show()
        self.retranslateUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
