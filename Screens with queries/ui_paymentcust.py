# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paymentcust.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget,QMessageBox)
import pyodbc
from datetime import datetime

class UI_Payment(QMainWindow):
    def __init__(self):
        super().__init__()
        self.orderno = 0
        self.total = 0
        self.cid = 0
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        

    def setValues(self,orderno,total,cid):
        
        self.orderno = orderno
        self.total = total
        self.cid = cid
        self.lineEdit_6.setText('{}'.format(self.orderno))
        self.lineEdit_7.setText('{}'.format(self.total))
        self.lineEdit_8.setText('{}'.format(self.total))
        self.comboBox.setFocus()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 324)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 170, 101, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 130, 71, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 240, 111, 24))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QRect(330, 70, 113, 51))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(200, 130, 71, 24))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(140, 80, 71, 24))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 170, 72, 24))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 80, 71, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(260, 80, 71, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 476, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.payment)
        self.lineEdit_6.returnPressed.connect(self.findorder)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Complete Payment", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Cash", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Credit", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Bank Transfer", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Order ID", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total", None))
    # retranslateUi
    def payment(self):
        cnxn = None
        payment_method = self.comboBox.currentText()
        entered_amount = float(self.lineEdit_8.text())

        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                # Check if entered amount is equal to the total
                if entered_amount == self.total:
                    # Insert transaction details
                    order_date = datetime.now().date().strftime('%Y-%m-%d')
                    order_time = datetime.now().time().strftime('%H:%M:%S')
                    cursor.execute("SELECT MAX(transactionID) FROM Customer_Transactions")
                    max_id_result = cursor.fetchone()
                    if max_id_result and max_id_result[0] is not None:
                        max_id = int(max_id_result[0])
                    else:
                        max_id = 0
                    new_tid = max_id + 1
                    cursor.execute("INSERT INTO Customer_Transactions VALUES (?, ?, ?,?,?,?)",
                                   new_tid,payment_method,entered_amount,self.orderno,order_date,order_time )

                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Payment Successful")
                    msg_box.setText("Payment completed successfully.")
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    result = msg_box.exec_()
                    self.close()
                    self.cleardata()
                    

                elif entered_amount < self.total:
                    # Check if customer is in credit table
                    cursor.execute("SELECT * FROM Credit_Customers WHERE customerID = ?", self.cid)
                    credit_row = cursor.fetchone()

                    if credit_row:
                        # Update credit amount
                        updated_credit = credit_row[2] + (self.total - entered_amount)
                        cursor.execute("UPDATE Credit_Customers SET totalCredit = ? WHERE creditCustomerID = ?",
                                       updated_credit, credit_row[1])
                    else:
                        cursor.execute("SELECT MAX(creditCustomerID) FROM Credit_Customers")
                        max_id = int(cursor.fetchone()[0]) if cursor.fetchone()[0] else 0
                        new_credit_customer_id = max_id + 1
                        # Add a new entry in the credit table
                        cursor.execute("INSERT INTO Credit_Customers VALUES (?, ?, ?)",
                                       new_credit_customer_id,self.cid, (self.total - entered_amount))
                        
                    order_date = datetime.now().date().strftime('%Y-%m-%d')
                    order_time = datetime.now().time().strftime('%H:%M:%S')
                    cursor.execute("SELECT MAX(transactionID) FROM Customer_Transactions")
                    max_id = int(cursor.fetchone()[0]) if cursor.fetchone()[0] else 0
                    new_tid = max_id + 1
                    # Insert transaction details
                    cursor.execute("INSERT INTO Customer_Transactions VALUES (?, ?, ?,?,?,?)",
                                   new_tid,payment_method,entered_amount,self.orderno,order_date,order_time )
                    cursor.execute("INSERT INTO Customer_Transactions VALUES (?, ?, ?,?,?,?)",
                                   new_tid+1,"Credit",(self.total - entered_amount),self.orderno,order_date,order_time )

                    # Show success message
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Payment Successful")
                    msg_box.setText("Partial payment completed successfully.")
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    result = msg_box.exec_()
                    self.cleardata()
                    

                else:
                    # Show error message if entered amount exceeds the total
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Payment Error")
                    msg_box.setText("Entered amount exceeds the total.")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    result = msg_box.exec_()
                    
                
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


    def cleardata(self):
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.comboBox.clear()
        self.pushButton.setEnabled(False)

    def findorder(self):
        cnxn = None
        id = self.lineEdit_6.text()
        self.lineEdit_6.setEnabled(False)
        total = 0
        totalpaid = 0
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("Select * from Customer_Order_Details Where orderId=?",id)
                rows = cursor.fetchall()
                for row in rows:
                    prodtot = 0
                    pid=row[1]
                    quantity= row[2]
                    cursor.execute("Select * from Products Where productID = ?",pid)
                    prodprice=cursor.fetchone()[2]
                    prodtot = int(quantity) * int(prodprice)
                    total = total + prodtot
                self.lineEdit_7.setText(str(total))
                cursor.execute("SELECT * FROM Customer_Transactions WHERE orderID = ? AND transactionType IN (?, ?)", (id, 'Cash', 'Bank Transfer'))
                rows = cursor.fetchall()
                for row in rows:
                    totalpaid = totalpaid + row[2]
                rem = total -totalpaid
                if rem == 0 :
                    self.lineEdit_8.setText(str(rem))
                    self.pushButton.setEnabled(False)
                else:
                    self.lineEdit_8.setText(str(rem))
                cursor.execute("Select * from Customer_Order Where orderID=?",id)
                self.cid = cursor.fetchone()[1]
            self.orderno = id
            self.total = total
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

    
