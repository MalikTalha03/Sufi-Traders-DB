# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew_Order = QAction(MainWindow)
        self.actionNew_Order.setObjectName(u"actionNew_Order")
        self.actionGet_Paid = QAction(MainWindow)
        self.actionGet_Paid.setObjectName(u"actionGet_Paid")
        self.actionFind_Order = QAction(MainWindow)
        self.actionFind_Order.setObjectName(u"actionFind_Order")
        self.actionUpdate_Customer = QAction(MainWindow)
        self.actionUpdate_Customer.setObjectName(u"actionUpdate_Customer")
        self.actionGet_All_Orders = QAction(MainWindow)
        self.actionGet_All_Orders.setObjectName(u"actionGet_All_Orders")
        self.actionNew_Order_2 = QAction(MainWindow)
        self.actionNew_Order_2.setObjectName(u"actionNew_Order_2")
        self.actionPay_Supplier = QAction(MainWindow)
        self.actionPay_Supplier.setObjectName(u"actionPay_Supplier")
        self.actionFind_Supplier = QAction(MainWindow)
        self.actionFind_Supplier.setObjectName(u"actionFind_Supplier")
        self.actionUpdate_details = QAction(MainWindow)
        self.actionUpdate_details.setObjectName(u"actionUpdate_details")
        self.actionAll_Orderd = QAction(MainWindow)
        self.actionAll_Orderd.setObjectName(u"actionAll_Orderd")
        self.actionFind_Order_2 = QAction(MainWindow)
        self.actionFind_Order_2.setObjectName(u"actionFind_Order_2")
        self.actionInventory = QAction(MainWindow)
        self.actionInventory.setObjectName(u"actionInventory")
        self.actionAdd_Category = QAction(MainWindow)
        self.actionAdd_Category.setObjectName(u"actionAdd_Category")
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionCheck_Details = QAction(MainWindow)
        self.actionCheck_Details.setObjectName(u"actionCheck_Details")
        self.actionUpdate_Details = QAction(MainWindow)
        self.actionUpdate_Details.setObjectName(u"actionUpdate_Details")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 131, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 80, 751, 421))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(230, 20, 141, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 510, 101, 21))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_Order.setText(QCoreApplication.translate("MainWindow", u"New Order", None))
        self.actionGet_Paid.setText(QCoreApplication.translate("MainWindow", u"Get Paid", None))
        self.actionFind_Order.setText(QCoreApplication.translate("MainWindow", u"Find Order", None))
        self.actionUpdate_Customer.setText(QCoreApplication.translate("MainWindow", u"Update Customer", None))
        self.actionGet_All_Orders.setText(QCoreApplication.translate("MainWindow", u"Get All Orders", None))
        self.actionNew_Order_2.setText(QCoreApplication.translate("MainWindow", u"New Order", None))
        self.actionPay_Supplier.setText(QCoreApplication.translate("MainWindow", u"Pay Supplier", None))
        self.actionFind_Supplier.setText(QCoreApplication.translate("MainWindow", u"Find Supplier", None))
        self.actionUpdate_details.setText(QCoreApplication.translate("MainWindow", u"Update details", None))
        self.actionAll_Orderd.setText(QCoreApplication.translate("MainWindow", u"All Orders", None))
        self.actionFind_Order_2.setText(QCoreApplication.translate("MainWindow", u"Find Order", None))
        self.actionInventory.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.actionAdd_Category.setText(QCoreApplication.translate("MainWindow", u"Add Category", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionCheck_Details.setText(QCoreApplication.translate("MainWindow", u"Check Details", None))
        self.actionUpdate_Details.setText(QCoreApplication.translate("MainWindow", u"Update Details", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Today Sales", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Monthly Sales", None))
    # retranslateUi

