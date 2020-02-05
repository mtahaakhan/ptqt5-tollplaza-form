from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
class Vehicle():
    def __init__(self,body_type,number_plate):
        self.body_type = body_type
        self.number_plate = number_plate
        self.conn = pyodbc.connect('Driver={SQL Server};'
                'Server=DESKTOP-VOPQDKG;'
                'Database=vehicle_detection;'
                'Trusted_Connection=yes;')
        self.status = False
        self.vehicle_box = QtWidgets.QMessageBox()
    
    def insert_vehicle(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"INSERT INTO dbo.Vehicles(body_type,number_plate) VALUES ('{self.body_type}','{self.number_plate}')")
            self.conn.commit()  
            self.conn.close()
            self.status = True
            self.message_box("Success", "Data has been added")
        except:
            self.message_box("Failed", "Data has not been added")
            self.status = False
    def message_box(self,title,message):
        self.vehicle_box.setWindowTitle(title)
        self.vehicle_box.setText(message)
        self.vehicle_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.vehicle_box.exec_()
        
        