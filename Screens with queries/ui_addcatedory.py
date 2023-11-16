# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcatedory.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pyodbc
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 70, 113, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 70, 71, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 150, 80, 24))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 110, 113, 24))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 110, 91, 16))
        self.pushButton.clicked.connect(self.addcategory)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Category ID", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Category ID", None))
    # retranslateUi
    def addcategory(self):
        cnxn = None
        cid = self.lineEdit.text()
        cname = self.lineEdit_2.text()
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
                cursor.execute("Insert into Categories values (?,?)", cid,cname)
                cursor.commit()
        except pyodbc.Error as ex:
            # Handle the exception and inform the user
            print("Database Error: ?",ex)
        finally:
            # Close the connection in the finally block
            if cnxn:
                cnxn.close()
                print("Connection closed.")



