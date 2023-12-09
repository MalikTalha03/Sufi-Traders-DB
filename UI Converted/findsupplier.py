from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from db import DatabaseManager
class Ui_Form(object):
    def __init__(self): 
        self.db = DatabaseManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(78, 110, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 190, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(78, 150, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 150, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 110, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 190, 101, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 230, 113, 22))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(80, 230, 101, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(40, 50, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit.returnPressed.connect(self.findbyid)
        self.lineEdit_2.returnPressed.connect(self.findbyname)
        self.lineEdit_3.returnPressed.connect(self.findbycontact)
        self.lineEdit.setFocus()
        self.lineEdit_4.setEnabled(False)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Supplier Details"))
        self.label.setText(_translate("Form", "Supplier ID"))
        self.label_2.setText(_translate("Form", "Supplier Name"))
        self.label_3.setText(_translate("Form", "Supplier Contact"))
        self.label_4.setText(_translate("Form", "Supplier Address"))
        self.label_5.setText(_translate("Form", "Enter any detail and PRESS Enter to get details"))

    def findbyid(self):
        id = self.lineEdit.text()
        rows = self.db.execute_read_query("SELECT * FROM Supplier WHERE supplierID = '{}'".format(id))
        if rows:
            for row in rows:
                self.lineEdit_2.setText(row[1])
                self.lineEdit_3.setText(row[3])
                self.lineEdit_4.setText(row[2])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Supplier Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()

    def findbyname(self):
        name = self.lineEdit_2.text()
        rows = self.db.execute_read_query("SELECT * FROM Supplier WHERE supplierName = '{}'".format(name))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_3.setText(row[3])
                self.lineEdit_4.setText(row[2])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Supplier Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
    def findbycontact(self):
        contact = self.lineEdit_3.text()
        rows = self.db.execute_read_query("SELECT * FROM Supplier WHERE supplierContact = '{}'".format(contact))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_2.setText(row[1])
                self.lineEdit_4.setText(row[2])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Supplier Not Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()          

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
