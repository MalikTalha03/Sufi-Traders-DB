# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paysupplier.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
import pyodbc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionadd = QAction(MainWindow)
        self.actionadd.setObjectName(u"actionadd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 81, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 71, 16))
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QRect(390, 40, 113, 24))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QRect(120, 70, 113, 24))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 40, 101, 20))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QRect(120, 40, 113, 24))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QRect(390, 10, 191, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(120, 10, 113, 24))
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
        self.tableWidget.setGeometry(QRect(10, 100, 761, 431))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(761, 431))
        self.tableWidget.setSortingEnabled(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 10, 91, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 530, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuoption = QMenu(self.menubar)
        self.menuoption.setObjectName(u"menuoption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuoption.menuAction())
        self.menuoption.addAction(self.actionadd)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionadd.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Amount", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Order No", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None))
        self.lineEdit_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Remaining Amount", None))
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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Supplier Name", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.menuoption.setTitle(QCoreApplication.translate("MainWindow", u"option", None))
    # retranslateUi

    def findorder(self):
        self.clearfields()
        cnxn = None
        id = self.lineEdit.text()
        total = 0
        totalpaid = 0
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("Select * from Customer_Order Where orderID=?",id)
                order = cursor.fetchone()
                if order:
                    cid = order[1]
                    self.lineEdit_8.setText(str(cid))
                    cursor.execute("Select * from Customers Where customerID=?",cid)
                    cust = cursor.fetchone()
                    if cust:
                        cname = str(cust[1] + " " + cust[2])
                        self.lineEdit_2.setText(cname)
                    cursor.execute("Select * from Customer_Order_Details Where orderId=?",id)
                    rows = cursor.fetchall()
                    for row in rows:
                        prodtot = 0
                        pid=row[1]
                        quantity= row[2]
                        cursor.execute("Select * from Products Where productID = ?",pid)
                        prod = cursor.fetchone()
                        prodprice=prod[2]
                        prodtot = int(quantity) * int(prodprice)
                        total = total + prodtot

                        row_position = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(row_position)
                        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(pid)))
                        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(prod[1])))
                        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(prodprice)))
                        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(quantity)))
                        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(prodtot)))
                    self.lineEdit_4.setText(str(total))
                    cursor.execute("SELECT * FROM Customer_Transactions WHERE orderID = ? AND transactionType IN (?, ?)", (id, 'Cash', 'Bank Transfer'))
                    rows = cursor.fetchall()
                    for row in rows:
                        totalpaid = totalpaid + row[2]
                        self.lineEdit_3.setText(str(totalpaid))
                    rem = total -totalpaid
                    if rem == 0 :
                        self.lineEdit_9.setText(str(rem))
                    else:
                        self.lineEdit_9.setText(str(rem))
                else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Order Error")
                    msg_box.setText("No Order Found against ID : {}".format(id))
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    result = msg_box.exec_()
                            
                
                

                
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Database Error")
            msg_box.setText("Error: {}".format(ex))
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setStandardButtons(QMessageBox.Ok)
            result = msg_box.exec_()
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()

