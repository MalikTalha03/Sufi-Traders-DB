from PyQt6 import QtCore, QtGui, QtWidgets
from db import DatabaseManager
class Ui_MainWindow(object):
    def __init__(self):
        self.db = DatabaseManager()
        self.id = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 150, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 150, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 190, 113, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 190, 131, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 230, 113, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 230, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 270, 131, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 270, 113, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 330, 80, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(parent=self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_order = QtGui.QAction(parent=MainWindow)
        self.actionAdd_order.setObjectName("actionAdd_order")
        self.actionadd = QtGui.QAction(parent=MainWindow)
        self.actionadd.setObjectName("actionadd")
        self.menuOptions.addAction(self.actionAdd_order)
        self.menuOptions.addAction(self.actionadd)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.pushButton.clicked.connect(self.addsupplier)
        self.lineEdit.returnPressed.connect(lambda:self.lineEdit_2.setFocus())
        self.lineEdit_2.returnPressed.connect(lambda:self.lineEdit_3.setFocus())
        self.lineEdit_3.returnPressed.connect(lambda:self.lineEdit_4.setFocus())
        self.idfind()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Supplier"))
        self.label.setText(_translate("MainWindow", "Supplier ID"))
        self.label_2.setText(_translate("MainWindow", "Supplier Name"))
        self.label_3.setText(_translate("MainWindow", "Supplier Contact"))
        self.label_4.setText(_translate("MainWindow", "Supplier Address"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionAdd_order.setText(_translate("MainWindow", "Add order"))
        self.actionadd.setText(_translate("MainWindow", "add"))

    def addsupplier(self):
        cnxn = None
        suppID = self.lineEdit.text()
        suppName = self.lineEdit_2.text()
        suppContact = self.lineEdit_3.text()
        suppAddress = self.lineEdit_4.text()
        rows = self.db.execute_read_query("Select * from Supplier where supplierName = '{}'".format(suppName))
        for row in rows:
            if row :
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Error")
                msg_box.setText("Supplier Already Exists.")
                msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                result = msg_box.exec()
            else:
                self.db.execute_query("Insert into Supplier values (?,?,?,?)", suppID,suppName,suppAddress,str(suppContact)) 
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Success")
                msg_box.setText("Supplier Added Successfully.")
                msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                result = msg_box.exec()
            MainWindow.close()

    def idfind(self):
        rows = self.db.execute_read_query("Select MAX(supplierID) From Supplier")
        for row in rows:
            if row and row[0] is not None:
                self.id = row[0] + 1
            else:
                self.id = 1
            self.lineEdit.setText(str(self.id))
            self.lineEdit.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())