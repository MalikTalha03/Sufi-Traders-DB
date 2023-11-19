# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplierOrder.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pyodbc
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
from datetime import datetime

class Ui_MainWindow(object):
    def __init__(self):
        self.total = 0  
        self.suppid = 0
        self.row_details = []
        self.category_data = {}
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        from ui_supporderdetail import SignalEmitter
        self.signal_emitter = SignalEmitter()
        self.signal_emitter.reset_variables_signal.connect(self.reset_variables)




    def open_details_window(self):
        from ui_supporderdetail import Ui_Window
        data_to_pass = self.row_details  # Assuming row_details is the data you want to pass
        self.details_window = Ui_Window(data_to_pass,self.suppid,self.total)
        self.details_window.show()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionOrder = QAction(MainWindow)
        self.actionOrder.setObjectName(u"actionOrder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 61, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 20, 81, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 60, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 60, 81, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 100, 81, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 100, 61, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 140, 49, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 20, 113, 24))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QRect(510, 20, 113, 24))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(140, 60, 113, 24))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QRect(510, 60, 113, 24))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(140, 100, 113, 24))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(510, 100, 113, 24))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(140, 140, 113, 24))
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
        self.tableWidget.setGeometry(QRect(50, 190, 721, 341))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QRect(650, 120, 111, 41))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(660, 90, 91, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(680, 530, 80, 24))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(390, 140, 61, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(510, 140, 111, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.actionAdd)
        self.menuOptions.addAction(self.actionOrder)
        self.lineEdit.returnPressed.connect(self.findsupplier)
        self.lineEdit_3.returnPressed.connect(self.findproduct)
        self.lineEdit_7.returnPressed.connect(self.addproduct)
        self.lineEdit_5.returnPressed.connect(self.movefocus)
        self.lineEdit_6.returnPressed.connect(self.nextfocus)
        self.lineEdit_4.returnPressed.connect(self.movenext)
        self.pushButton.clicked.connect(self.open_details_window)
        self.fetch_and_populate_categories()
        self.comboBox.activated.connect(self.handle_category_selection)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def nextfocus(self):
        if self.lineEdit_6.text():
            self.lineEdit_7.setFocus()

    def movenext(self):
        if self.lineEdit_4.text():
            self.lineEdit_5.setFocus()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionOrder.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Supplier ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Supplier Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Product ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Purchase Price", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sale Price", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
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
        self.lineEdit_8.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Grand Total", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Category", None))

        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

    def movefocus(self):
        self.lineEdit_6.setFocus()

    def findsupplier(self):
        cnxn = None
        
        id = self.lineEdit.text()
        
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT * FROM Supplier WHERE supplierID = ?", id)
                row = cursor.fetchone()
                if row:
                    self.lineEdit_2.setText(row[1])
                    self.lineEdit_3.setFocus()
                else:
                    # Inform the user that no entry was found
                    print("No Entry Found")
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error ?",ex)
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")
            

    def findproduct(self):
        cnxn = None
        pid = self.lineEdit_3.text()
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT * FROM Products WHERE productID = ?", pid)
                row = cursor.fetchone()
                if row:
                    self.lineEdit_4.setText(str(row[1]))
                    self.lineEdit_4.setEnabled(False)
                    self.lineEdit_6.setText(str(row[2]))

                    category_id = row[3]
                    category_name = self.get_key_by_value(category_id)
                    index = self.comboBox.findText(category_name)
                    print(category_name )
                    if index != -1:
                        self.comboBox.setCurrentIndex(index)
                        self.comboBox.setEnabled(False)
                    self.lineEdit_5.setFocus()
                else:
                    self.lineEdit_4.setFocus()
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error ?", ex)
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")

    def get_key_by_value(self,target_value):
        for key, value in self.category_data.items():
            if value == target_value:
                return key
        return None 


    def addproduct(self):
        cnxn = None
        if (
            self.lineEdit.text() and self.lineEdit_3.text() and self.lineEdit_4.text()
            and self.lineEdit_6.text() and self.lineEdit_7.text() and self.comboBox.currentIndex() >= 0):

            pid = self.lineEdit_3.text()
            pname = self.lineEdit_4.text()
            saleprice = float(self.lineEdit_6.text())
            inv = int(self.lineEdit_7.text())
            self.suppid = self.lineEdit.text()
            purprice = float(self.lineEdit_5.text())
            selected_category_name = self.comboBox.currentText()
            cid = self.category_data.get(selected_category_name, "Unknown Category")
            total_price = purprice * inv

            # Check if the product is already in the list
            existing_product_index = -1
            for i, row_detail in enumerate(self.row_details):
                if row_detail['pid'] == pid:
                    existing_product_index = i
                    break

            if existing_product_index != -1:
                # Product already exists, update inventory and table entry
                existing_inv = self.row_details[existing_product_index]['inv']
                self.row_details[existing_product_index]['inv'] += inv
                self.row_details[existing_product_index]['total_price'] += total_price

                # Update the table widget
                self.tableWidget.setItem(existing_product_index, 4, QTableWidgetItem(str(existing_inv + inv)))
                self.tableWidget.setItem(existing_product_index, 5, QTableWidgetItem(str(self.row_details[existing_product_index]['total_price'])))

            else:
                # Product does not exist, add a new row to the table widget
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QTableWidgetItem(pid))
                self.tableWidget.setItem(row_position, 1, QTableWidgetItem(selected_category_name))
                self.tableWidget.setItem(row_position, 2, QTableWidgetItem(pname))
                self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(purprice)))
                self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(inv)))
                self.tableWidget.setItem(row_position, 5, QTableWidgetItem(str(total_price)))

                # Update the total
                self.total += total_price
                self.lineEdit_8.setText(str(self.total))

                # Add the new product to the list
                row_detail = {
                    'pid': pid,
                    'pname': pname,
                    'purprice': purprice,
                    'inv': inv,
                    'total_price': total_price,
                    'sale_price': saleprice,
                    'cid': cid,
                    'cname': selected_category_name,
                }
                self.row_details.append(row_detail)

            # Clear the line edits
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.comboBox.clear()
            self.lineEdit_4.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.fetch_and_populate_categories()
            self.lineEdit_3.setFocus()
            print(row_detail)

    def fetch_and_populate_categories(self):
        cnxn = None
        try:
            # Connect to the database
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                # Execute a query to fetch category IDs and names
                cursor.execute("SELECT * FROM Categories")
                rows = cursor.fetchall()
                self.category_data = {row[1]: row[0] for row in rows}
                # Populate the ComboBox with category names
                for row in rows:
                    category_name = row[1]
                    self.comboBox.addItem(category_name)

        except pyodbc.Error as ex:
            print("Database Error:", ex)
        finally:
            if cnxn:
                cnxn.close()

    def handle_category_selection(self, index):
        # Get the selected category name
        selected_category_name = self.comboBox.currentText()

        # Get the category ID using the selected category name
        selected_category_id = self.category_data.get(selected_category_name, None)

        if selected_category_id is not None:
            print("Selected Category ID:", selected_category_id)
        else:
            print("Category ID not found for:", selected_category_name)


