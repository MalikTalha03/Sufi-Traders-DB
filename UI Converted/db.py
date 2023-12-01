# database_manager.py

import pyodbc
from PyQt6 import QtWidgets

class DatabaseManager:
    def __init__(self):
        self.cnxn_str = (
            "Driver={SQL Server};"
            "Server=MALIK-TALHA;"
            "Database=Sufi_Traders;"
            "Trusted_Connection=yes;"
        )
        try: 
            self.db = pyodbc.connect(self.cnxn_str)
            self.cursor = self.db.cursor()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Database Connection Error")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.db.commit()

    
    def execute_read_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def close_connection(self):
        self.db.close()

    