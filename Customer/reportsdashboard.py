# Form implementation generated from reading ui file 'reportsdashboard.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(210, 20, 89, 20))
        self.radioButton.setObjectName("radioButton")
        self.type = QtWidgets.QButtonGroup(MainWindow)
        self.type.setObjectName("type")
        self.type.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 20, 89, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.type.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(470, 20, 89, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.type.addButton(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(620, 20, 89, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.type.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(490, 80, 131, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.salessub = QtWidgets.QButtonGroup(MainWindow)
        self.salessub.setObjectName("salessub")
        self.salessub.addButton(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(340, 80, 131, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.salessub.addButton(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(180, 80, 141, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.salessub.addButton(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(650, 80, 131, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.salessub.addButton(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(30, 80, 121, 20))
        self.radioButton_9.setObjectName("radioButton_9")
        self.salessub.addButton(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(160, 140, 89, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.datebtn = QtWidgets.QButtonGroup(MainWindow)
        self.datebtn.setObjectName("datebtn")
        self.datebtn.addButton(self.radioButton_10)
        self.radioButton_12 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(280, 140, 89, 20))
        self.radioButton_12.setObjectName("radioButton_12")
        self.datebtn.addButton(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(420, 140, 89, 20))
        self.radioButton_13.setObjectName("radioButton_13")
        self.datebtn.addButton(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_14.setGeometry(QtCore.QRect(30, 140, 89, 20))
        self.radioButton_14.setObjectName("radioButton_14")
        self.datebtn.addButton(self.radioButton_14)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(540, 140, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(680, 140, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 140, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_15 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_15.setGeometry(QtCore.QRect(210, 360, 89, 20))
        self.radioButton_15.setObjectName("radioButton_15")
        self.charts = QtWidgets.QButtonGroup(MainWindow)
        self.charts.setObjectName("charts")
        self.charts.addButton(self.radioButton_15)
        self.radioButton_11 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(380, 360, 89, 20))
        self.radioButton_11.setObjectName("radioButton_11")
        self.charts.addButton(self.radioButton_11)
        self.radioButton_17 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_17.setGeometry(QtCore.QRect(530, 360, 89, 20))
        self.radioButton_17.setObjectName("radioButton_17")
        self.charts.addButton(self.radioButton_17)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 500, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 500, 111, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 500, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 101, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 220, 111, 22))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Report Type"))
        self.radioButton.setText(_translate("MainWindow", "Sales"))
        self.radioButton_2.setText(_translate("MainWindow", "Financial"))
        self.radioButton_3.setText(_translate("MainWindow", "Customer"))
        self.radioButton_4.setText(_translate("MainWindow", "Inventory"))
        self.radioButton_5.setText(_translate("MainWindow", "By Customer"))
        self.radioButton_6.setText(_translate("MainWindow", "By Product"))
        self.radioButton_7.setText(_translate("MainWindow", "By Employee"))
        self.radioButton_8.setText(_translate("MainWindow", "By Category"))
        self.radioButton_9.setText(_translate("MainWindow", "Total Sales"))
        self.radioButton_10.setText(_translate("MainWindow", "This Month"))
        self.radioButton_12.setText(_translate("MainWindow", "This Year"))
        self.radioButton_13.setText(_translate("MainWindow", "Date Range"))
        self.radioButton_14.setText(_translate("MainWindow", "Today"))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.radioButton_15.setText(_translate("MainWindow", "Bar Chart"))
        self.radioButton_11.setText(_translate("MainWindow", "Pie Chart"))
        self.radioButton_17.setText(_translate("MainWindow", "Line Chart"))
        self.label_3.setText(_translate("MainWindow", "Report Visuals"))
        self.pushButton.setText(_translate("MainWindow", "Download as PDF"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Employee Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())