# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addemployee.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget,QMessageBox)
import pyodbc

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-JS0EJFG\SQLEXPRESS;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(422, 391)
        self.actionoption = QAction(MainWindow)
        self.actionoption.setObjectName(u"actionoption")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 40, 113, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(68, 40, 71, 20))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 120, 113, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 120, 91, 20))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 80, 113, 24))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 80, 71, 20))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(170, 160, 113, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 160, 71, 20))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(170, 200, 113, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 200, 71, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 240, 71, 20))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 240, 72, 24))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 300, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 21))
        self.menuadd = QMenu(self.menubar)
        self.menuadd.setObjectName(u"menuadd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuadd.menuAction())
        self.menuadd.addAction(self.actionoption)
        self.pushButton.clicked.connect(self.addemployee)
        self.lineEdit.returnPressed.connect(lambda: self.lineEdit_3.setFocus())
        self.lineEdit_2.returnPressed.connect(lambda: self.lineEdit_4.setFocus())
        self.lineEdit_3.returnPressed.connect(lambda: self.lineEdit_2.setFocus())
        self.lineEdit_4.returnPressed.connect(lambda: self.lineEdit_5.setFocus())
        self.lineEdit_5.returnPressed.connect(lambda: self.comboBox.setFocus())  # No next line edit for the last one

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionoption.setText(QCoreApplication.translate("MainWindow", u"option", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lineEdit_5.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Employee", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u" CEO", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.menuadd.setTitle(QCoreApplication.translate("MainWindow", u"add", None))
    # retranslateUi

    def addemployee(self):
        fname = self.lineEdit.text()
        lname = self.lineEdit_3.text()
        contact = self.lineEdit_2.text()
        address = self.lineEdit_4.text()
        salary = self.lineEdit_5.text()
        typee =  self.comboBox.currentText()
        cnxn = None
        try:
            # Assign the connection to cnxn
            cnxn = pyodbc.connect(self.cnxn_str)
            with cnxn.cursor() as cursor:
                cursor.execute("SELECT MAX(employeeID) FROM Employee")
                max_order_id = cursor.fetchone()[0]

                if max_order_id is not None:
                    self.order_id = int(max_order_id) + 1
                else:
                    # If the table is empty, start with order ID 1
                    self.order_id = 1
                cursor.execute("INSERT into Employee Values(?,?,?,?,?,?,?)",self.order_id,fname,lname,contact,address,salary,typee)
                cursor.commit()
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Employee Added")
                msg_box.setText("Employee Added Successfully..")
                msg_box.setIcon(QMessageBox.Information)
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
