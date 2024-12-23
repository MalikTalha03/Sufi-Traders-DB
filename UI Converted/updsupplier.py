from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager

class Ui_Form(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(45, 10, 281, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(70, 180, 101, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 140, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 220, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(68, 100, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 180, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(68, 140, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 100, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 101, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 250, 91, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit.returnPressed.connect(self.findbyid)
        self.lineEdit.setFocus()
        self.lineEdit_2.returnPressed.connect(self.findbyname)
        self.lineEdit_4.returnPressed.connect(self.findbycontact)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Update Supplier Details"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Enter any of given requirment and press enter to find Supplier Details</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Address"))
        self.label.setText(_translate("Form", "Supplier ID"))
        self.label_2.setText(_translate("Form", "Supplier Name"))
        self.label_4.setText(_translate("Form", "Contact"))
        self.pushButton.setText(_translate("Form", "Update"))
    
    def findbyid(self):
        rows = self.db.execute_read_query("Select * from Supplier where supplierID='{}'".format(self.lineEdit.text()))
        if rows:
            for row in rows:
                self.lineEdit_2.setText(row[1])
                self.lineEdit_3.setText(row[2])
                self.lineEdit_4.setText(str(row[3]))
                self.pushButton.clicked.connect(self.update)
                self.lineEdit.setEnabled(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("No Supplier Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowTitle("Warning")
            msg.exec()

    def update(self):
        if self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setText("Please Fill All Fields")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowTitle("Warning")
            msg.exec()
            return
        self.db.execute_query("UPDATE Supplier SET supplierName = '{}', supplierAddress = '{}', supplierContact = '{}' WHERE supplierID = '{}'".format(self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit.text()))
        msg = QtWidgets.QMessageBox()
        msg.setText("Supplier Updated Successfully")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.setWindowTitle("Success")
        msg.exec()
        Form.close()
        
    def findbyname(self):
        if self.lineEdit_2.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setText("Please Fill Supplier Name")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowTitle("Warning")
            msg.exec()
            return
        rows = self.db.execute_read_query("Select * from Supplier where supplierName='{}'".format(self.lineEdit_2.text()))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_3.setText(row[2])
                self.lineEdit_4.setText(str(row[3]))
                self.pushButton.clicked.connect(self.update)
                self.lineEdit.setEnabled(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("No Supplier Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowTitle("Warning")
            msg.exec()

    def findbycontact(self):
        if self.lineEdit_4.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setText("Please Fill Supplier Contact Number")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowTitle("Warning")
            msg.exec()
            return
        rows = self.db.execute_read_query("Select * from Supplier where supplierContact='{}'".format(self.lineEdit_4.text()))
        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[0]))
                self.lineEdit_2.setText(row[1])
                self.lineEdit_3.setText(row[2])
                self.pushButton.clicked.connect(self.update)
                self.lineEdit.setEnabled(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("No Supplier Found")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowTitle("Warning")
            msg.exec()
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
