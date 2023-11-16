# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supporderdetail.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)
from ui_supplierOrder import Ui_MainWindow as DetailsWindow

from PyQt5.QtCore import QObject, pyqtSignal

class SignalEmitter(QObject):
    reset_variables_signal = pyqtSignal()


class Ui_Window(QMainWindow, DetailsWindow):
    def __init__(self, data,suppid,orderno,total):
        super(Ui_Window, self).__init__()
        self.setupUi(self)
        self.total = total
        self.data = data
        self.suppid=suppid
        self.orderno=orderno
        self.populate_table()
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )


    def populate_table(self):
    # Assuming that self.data is a list of dictionaries
        for row_num, row_data in enumerate(self.data):
            # Add a new row to the table widget
            self.tableWidget.insertRow(row_num)

            # Define the keys you want to access
            keys_to_access = ['pid', 'cname', 'pname', 'purprice', 'inv', 'total_price']

            # Loop through the keys and set the items using the keys
            for col_num, col_key in enumerate(keys_to_access):
                item = QTableWidgetItem(str(row_data.get(col_key, '')))
                self.tableWidget.setItem(row_num, col_num, item)


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 721, 471))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 510, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOption.menuAction())
        self.menuOption.addAction(self.actionAdd)
        self.pushButton.clicked.connect(self.addtodb)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
    # retranslateUi

    def addtodb(self):
        cnxn = None
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("Insert into Supplier_Order Values (?,?,?,?)", self.orderno,datetime.today().strftime('%Y-%m-%d'),self.suppid,self.total)
                for data in self.data:
                    # Check if the product already exists
                    cursor.execute(
                        "SELECT * FROM Products WHERE productID = ?", data['pid'])
                    existing_product = cursor.fetchone()

                    if existing_product is not None:
                        # Product already exists, update quantity or price
                        new_quantity = existing_product[5] + data['inv']
                        new_price = data['sale_price']  # You can modify this according to your requirements

                        cursor.execute(
                            "UPDATE Products SET inventory = ?, salePrice = ? "
                            "WHERE productID = ?",
                            new_quantity, new_price, data['pid']
                        )
                        cursor.execute("Insert into Supplier_Order_Details Values (?,?,?,?)",
                                       self.orderno,data['pid'],data['purprice'],data['inv'])
                    else:
                        # Product doesn't exist, insert a new record
                        cursor.execute(
                            "INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?)",
                            data['pid'], data['pname'], data['sale_price'],
                            data['cid'], self.suppid, data['inv']
                        )
                        cursor.execute("Insert into Supplier_Order_Details Values (?,?,?,?)",
                                       self.orderno,data['pid'],data['purprice'],data['inv'])
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

