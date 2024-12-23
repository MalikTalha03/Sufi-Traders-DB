from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
class Ui_Form(object):
    def __init__(self):
        self.db = DatabaseManager()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 241)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 113, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 140, 113, 22))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit.returnPressed.connect(self.findbyid)
        self.lineEdit_2.returnPressed.connect(self.findbyname)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inventory"))
        self.label.setText(_translate("Form", "Product ID"))
        self.label_2.setText(_translate("Form", "Product Name"))
        self.label_3.setText(_translate("Form", "Available Stock"))
        
    def findbyid(self):
        id = self.lineEdit.text()
        rows = self.db.execute_read_query("SELECT * FROM Products WHERE ProductID = {}".format(id))
        if rows:
            for row in rows:
                    self.lineEdit_2.setText(str(row[1]))
                    self.lineEdit_3.setText(str(row[5]))
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("No Product Found")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()

    def findbyname(self):
        name = self.lineEdit_2.text()
        rows = self.db.execute_read_query("SELECT * FROM Products WHERE productName = '{}'".format(name))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_3.setText(str(row[5]))
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("No Product Found")
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            result = msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
