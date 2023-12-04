from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from db import DatabaseManager

class Ui_Form(object):
    def __init__(self) :
        super().__init__()
        self.db = DatabaseManager()
        self.id = 0
        self.idfind()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 110, 113, 24))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit.setText('{}'.format(str(self.id)))
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setFocus()
        self.pushButton.clicked.connect(self.addcategory)
        self.lineEdit.returnPressed.connect(lambda: self.lineEdit_2.setFocus())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Category ID"))
        self.pushButton.setText(_translate("Form", "ADD"))
        self.label_2.setText(_translate("Form", "Category Name"))
    
    def idfind(self):
        rows = self.db.execute_read_query("Select MAX(categoryID) From Categories")
        for row in rows:
            if row and row[0] is not None:
                self.id = row[0] + 1
            else:
                self.id = 1

    def addcategory(self):
        cid = self.lineEdit.text()
        cname = self.lineEdit_2.text()
        rows = self.db.execute_query("Insert into Categories values ({},'{}')".format(cid,cname))
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_box.setText("Category added successfully .")
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = msg_box.exec()
        Form.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
