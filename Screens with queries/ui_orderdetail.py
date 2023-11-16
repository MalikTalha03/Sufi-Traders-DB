# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderdetail.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pyodbc
from datetime import datetime
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
from ui_form  import Ui_MainWindow as DetailsWindow
from PyQt5.QtCore import QObject, pyqtSignal

class SignalEmitter(QObject):
    reset_variables_signal = pyqtSignal()


class Ui_MainWin(QMainWindow, DetailsWindow):
    def __init__(self, data,order,custid,total):
        super(Ui_MainWin, self).__init__()
        self.setupUi(self)
        self.total = total
        self.data = data
        self.cid=custid
        self.orderno=order
        self.populate_table()
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionadd = QAction(MainWindow)
        self.actionadd.setObjectName(u"actionadd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(670, 520, 80, 24))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QRect(570, 10, 113, 51))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QRect(110, 30, 113, 24))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(470, 30, 71, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 30, 71, 16))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 761, 431))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(761, 431))
        self.tableWidget.setSortingEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuoptions = QMenu(self.menubar)
        self.menuoptions.setObjectName(u"menuoptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuoptions.menuAction())
        self.menuoptions.addAction(self.actionadd)
        self.pushButton.clicked.connect(self.addtodb)
        

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionadd.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Order ID", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Per unit Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.menuoptions.setTitle(QCoreApplication.translate("MainWindow", u"options", None))
    # retranslateUi
    def populate_table(self):
        self.lineEdit_6.setText('{}'.format(self.orderno))
        self.lineEdit_7.setText('{}'.format(self.total))
    # Assuming that self.data is a list of dictionaries
        for row_num, row_data in enumerate(self.data):
            # Add a new row to the table widget
            self.tableWidget.insertRow(row_num)

            # Define the keys you want to access
            keys_to_access = ['pid', 'pname', 'price', 'quantity', 'total_price']

            # Loop through the keys and set the items using the keys
            for col_num, col_key in enumerate(keys_to_access):
                item = QTableWidgetItem(str(row_data.get(col_key, '')))
                self.tableWidget.setItem(row_num, col_num, item)

    def addtodb(self):
        cnxn = None
        order_date = datetime.now().date().strftime('%Y-%m-%d')
        order_time = datetime.now().time().strftime('%H:%M:%S')
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("INSERT INTO Customer_Order (orderID, customerID, employeeID, orderDate, orderTime) VALUES (?, ?, ?, ?, ?)",self.orderno, self.cid, 1, order_date, order_time)                
                for data in self.data:
                    # Check if the product already exists
                    cursor.execute(
                        "SELECT * FROM Products WHERE productID = ?", data['pid'])
                    existing_product = cursor.fetchone()

                    if existing_product is not None:
                        # Product already exists, update quantity or price
                        new_quantity = int(existing_product[5]) - int(data['quantity'])

                        cursor.execute(
                            "UPDATE Products SET inventory = ? WHERE productID = ?",
                            new_quantity, data['pid']
                        )
                        cursor.execute("Insert into Customer_Order_Details Values (?,?,?)",
                                       self.orderno,data['pid'],data['quantity'])
                cursor.commit()
            # Clear the list after successfully adding to the database
            self.total = 0
            self.data = []
            self.suppid=0
            self.orderno=0
            self.emit_reset_variables_signal()
            self.close()
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error: ?", ex)
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")

    def emit_reset_variables_signal(self):
        # Emit the reset variables signal
        self.signal_emitter.reset_variables_signal.emit()

