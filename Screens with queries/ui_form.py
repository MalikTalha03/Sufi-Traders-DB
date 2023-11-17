# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,QMessageBox,
    QWidget)


class Ui_MainWindow(object):
    def __init__(self):
        self.row_details = []
        self.category_data = {}
        self.order_id = 0
        self.total = 0  # initialize total in the __init__ method
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        self.orderid()
        from ui_orderdetail import SignalEmitter
        self.signal_emitter = SignalEmitter()
        self.signal_emitter.reset_variables_signal.connect(self.reset_variables)
    
    def orderid(self):
        cnxn = None
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT MAX(orderID) FROM Customer_Order")
                max_order_id = cursor.fetchone()[0]

                if max_order_id is not None:
                    self.order_id = int(max_order_id) + 1
                else:
                    # If the table is empty, start with order ID 1
                    self.order_id = 1

        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: ?",ex)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setStandardButtons(QMessageBox.Ok)
            result = msg_box.exec_()
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")


    def reset_variables(self):
        self.close()
        print("closing....")

        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_Order = QAction(MainWindow)
        self.actionAdd_Order.setObjectName(u"actionAdd_Order")
        self.actionFiond_Order = QAction(MainWindow)
        self.actionFiond_Order.setObjectName(u"actionFiond_Order")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(400, 70, 113, 24))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(550, 70, 71, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 81, 16))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QRect(640, 70, 113, 24))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(550, 20, 71, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 71, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 71, 16))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QRect(640, 10, 113, 51))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(400, 10, 113, 24))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 70, 71, 16))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 40, 113, 24))
        self.lineEdit_3.setFocus()
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(130, 70, 113, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(130, 10, 113, 24))
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
        self.tableWidget.setGeometry(QRect(20, 100, 761, 431))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(761, 431))
        self.tableWidget.setSortingEnabled(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 10, 71, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 530, 80, 24))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 40, 71, 16))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(400, 40, 113, 24))
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
        self.lineEdit_6.setText("{}".format(self.order_id))

        
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.actionAdd_Order)
        self.menuOptions.addAction(self.actionFiond_Order)
        self.lineEdit_4.returnPressed.connect(self.move)
        self.lineEdit_5.returnPressed.connect(self.addNewRow)
        self.lineEdit_3.returnPressed.connect(self.handle_lineEdit3_enter) #listen enter
        self.pushButton.clicked.connect(self.open_details_window)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def move(self):
        self.lineEdit_5.setFocus()

    def addNewRow(self):
    # Get data from line edits
        product_name = self.lineEdit_4.text()
        quantity = self.lineEdit_5.text()
        
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT * FROM Products WHERE productName = ?", product_name)
                row = cursor.fetchone()
                
                if row:
                    if int(quantity) <= row[5]:
                        for row_num in range(self.tableWidget.rowCount()):
                            if self.tableWidget.item(row_num, 0).text() == str(row[0]):
                                current_quantity = int(self.tableWidget.item(row_num, 3).text())
                                new_quantity = current_quantity + int(quantity)

                                if new_quantity <= row[5]:  # Check if there is enough stock available
                                    self.tableWidget.setItem(row_num, 3, QTableWidgetItem(str(new_quantity)))

                                    product_price = row[2]  # price will be fetched from db
                                    total_price = product_price * new_quantity
                                    self.tableWidget.setItem(row_num, 4, QTableWidgetItem(str(total_price)))

                                    self.total += product_price * int(quantity)
                                    self.lineEdit_7.setText(str(self.total))

                                    for detail in self.row_details:
                                        if detail['pid'] == row[0]:
                                            detail['quantity'] = new_quantity
                                            detail['total_price'] = total_price

                                    print(self.row_details)
                                    # Clear the line edits
                                    self.lineEdit_5.clear()
                                    self.lineEdit_4.clear()
                                    self.lineEdit_4.setFocus()
                                    return  # Exit the function since the product is already in the list

                                else:
                                    self.showStockIssueMessageBox(row[5])
                                    return  # Exit the function since there is not enough stock

                        # If the loop completes without returning, it means the product is not in the list
                        self.addNewProductRow(row, quantity)

                    else:
                        self.showStockIssueMessageBox(row[5])
                else:
                    # Inform the user that no entry was found
                    print("No Entry Found")
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error")
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")
            # Add your logic here


    def addNewProductRow(self, row, quantity):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(row[0])))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(row[1])))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(quantity))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(row[2])))

        product_price = row[2]  # price will be fetched from db
        total_price = product_price * int(quantity)
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(total_price)))

        self.total += product_price * int(quantity)
        self.lineEdit_7.setText(str(self.total))

        row_detail = {
            'pid': row[0],
            'pname': row[1],
            'quantity': quantity,
            'total_price': total_price,
            'price': row[2]
        }
        self.row_details.append(row_detail)

        print(self.row_details)
        # Clear the line edits
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.lineEdit_4.setFocus()

    def showStockIssueMessageBox(self, available_stock):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Stock Issue")
        msg_box.setText("Stock Not available.\n{} pieces available in stock".format(available_stock))
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)

        result = msg_box.exec_()


        
        
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_Order.setText(QCoreApplication.translate("MainWindow", u"Add Order", None))
        self.actionFiond_Order.setText(QCoreApplication.translate("MainWindow", u"Find Order", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Order ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contact No.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi
    def handle_lineEdit3_enter(self):
    # Initialize cnxn to None
        cnxn = None
        
        phone = self.lineEdit_3.text()
        
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT * FROM Customers WHERE customerContact = ?", phone)
                row = cursor.fetchone()
                if row:
                    self.lineEdit.setText(row[1])
                    self.lineEdit_2.setText(row[2])
                    self.lineEdit_8.setText(str(row[0]))
                    self.lineEdit.setEnabled(False)
                    self.lineEdit_2.setEnabled(False)
                    self.lineEdit_8.setEnabled(False)
                    self.lineEdit_4.setFocus()
                else:
                    # Inform the user that no entry was found
                    print("No Entry Found")
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error")
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")
            # Add your logic here

    def open_details_window(self):
        from ui_orderdetail import Ui_MainWin
        data_to_pass = self.row_details  # Assuming row_details is the data you want to pass
        self.details_window = Ui_MainWin(data_to_pass,self.order_id,self.lineEdit_8.text(),self.total)
        self.details_window.show()



