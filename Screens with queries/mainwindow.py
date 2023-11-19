# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_addsupplier import Ui_MainWindow as Ui_AddSupplier  # Import the Ui_MainWindow class from ui_addsupplier.py
from ui_addcatedory import Ui_Form as category
from ui_supplierOrder import Ui_MainWindow as supporder 
from ui_findcustorder import Ui_MainWindow as order
from ui_form import Ui_MainWindow as addorder
from ui_paymentcust import UI_Payment as paycust
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = order()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
