# Form implementation generated from reading ui file 'findcust.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc

class Ui_Form(object):
    def __init__(self):
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=MALIK-TALHA;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(78, 130, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(78, 170, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 170, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 101, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 210, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit.returnPressed.connect(self.findbyid)
        self.lineEdit_2.returnPressed.connect(self.findbyname)
        self.lineEdit_3.returnPressed.connect(self.findbycontact)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Customer ID"))
        self.label_2.setText(_translate("Form", "Customer Name"))
        self.label_3.setText(_translate("Form", "Customer Contact"))
        self.label_4.setText(_translate("Form", "Enter ID or Name and Press Enter to retrieve Details"))
    def findbyid(self):
        id = self.lineEdit.text()
        cnxn = None
        try:
            with pyodbc.connect(self.cnxn_str) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM Customers WHERE customerID = ?", id
                    )
                    row = cursor.fetchone()
                    if row:
                        self.lineEdit_2.setText(row[1] + " " + row[2])
                        self.lineEdit_3.setText(row[3])
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Customer Not Found")
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                        msg.exec()
        except pyodbc.Error as ex:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Database Error: {}".format(ex))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        finally:
            if cnxn:
                cnxn.close()
    def findbyname(self):
        name = self.lineEdit_2.text()
        firstname = name.split(" ")[0]
        lastname = name.split(" ")[1]
        cnxn = None
        try:
            with pyodbc.connect(self.cnxn_str) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM Customers WHERE custFName = ? AND custLName = ?", firstname, lastname
                    )
                    row = cursor.fetchone()
                    if row:
                        self.lineEdit_2.setText(row[1] + " " + row[2])
                        self.lineEdit.setText(str(row[0]))
                        self.lineEdit_3.setText(row[3])
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Customer Not Found")
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                        msg.exec()
        except pyodbc.Error as ex:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Database Error: {}".format(ex))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        finally:
            if cnxn:
                cnxn.close()
    def findbycontact(self):
        contact = self.lineEdit_3.text()
        cnxn = None
        try:
            with pyodbc.connect(self.cnxn_str) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM Customers WHERE customerContact = ?", contact
                    )
                    row = cursor.fetchone()
                    if row:
                        self.lineEdit.setText(str(row[0]))
                        self.lineEdit_2.setText(row[1] + " " + row[2])
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Customer Not Found")
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                        msg.exec()
        except pyodbc.Error as ex:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Database Error: {}".format(ex))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        finally:
            if cnxn:
                cnxn.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())