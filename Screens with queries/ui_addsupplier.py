# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addsupplier.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_order = QAction(MainWindow)
        self.actionAdd_order.setObjectName(u"actionAdd_order")
        self.actionadd = QAction(MainWindow)
        self.actionadd.setObjectName(u"actionadd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 150, 113, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 150, 131, 16))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(380, 190, 113, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 190, 131, 16))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(380, 230, 113, 24))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 230, 131, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 270, 131, 16))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(380, 270, 113, 24))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 330, 80, 24))
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
        self.menuOptions.addAction(self.actionAdd_order)
        self.menuOptions.addAction(self.actionadd)
        self.pushButton.clicked.connect(self.handleButtonClick)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_order.setText(QCoreApplication.translate("MainWindow", u"Add order", None))
        self.actionadd.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Supplier ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Supplier Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Supplier Contact", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Supplier Address", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

    def handleButtonClick(self):
        cnxn = None
        suppID = self.lineEdit.text()
        suppName = self.lineEdit_2.text()
        suppContact = self.lineEdit_3.text()
        suppAddress = self.lineEdit_4.text()
        cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("Insert into Supplier values (?,?,?,?)", suppID,suppName,suppAddress,str(suppContact))
                cursor.commit()
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error: ?",ex)
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")

