from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
import pyodbc
from db import DatabaseManager
class Ui_Form(object):
    def __init__(self):
        self.db = DatabaseManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(338, 315)
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(60, 40, 71, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 240, 113, 24))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 160, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 40, 113, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 71, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 200, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 71, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 80, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(58, 80, 71, 20))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 120, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6.returnPressed.connect(self.findbyid)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Employee ID"))
        self.label_2.setText(_translate("Form", "Contact Number"))
        self.label_4.setText(_translate("Form", "Address"))
        self.label_3.setText(_translate("Form", "Last Name"))
        self.label_5.setText(_translate("Form", "Salary"))
        self.label.setText(_translate("Form", "First Name"))
    def findbyid(self):
        id = self.lineEdit_6.text()
        rows = self.db.execute_read_query("SELECT * FROM Employee WHERE employeeID = {}".format(id))

        if rows:
            for row in rows:
                self.lineEdit.setText(str(row[1]))
                self.lineEdit_3.setText(str(row[2]))
                self.lineEdit_2.setText(str(row[3]))
                self.lineEdit_4.setText(str(row[4]))
                self.lineEdit_5.setText(str(row[5]))
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("No Employee Found")
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
