from PyQt5 import QtCore, QtGui, QtWidgets
from vehicle import *

class Ui_MainWindow(object):

    def messagebox(self, title, message):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle(title)
        self.message.setText(message)
        self.message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.message.exec_()

    def save_vehicle_records(self):
        vehicle_number_plate = self.number_plate_input.text()
        vehicle_body_type = self.body_type_input.text()
        new_vehicle = Vehicle(vehicle_number_plate,vehicle_body_type)
        new_vehicle.insert_vehicle()
        # if new_vehicle.status:
            #form reset
        # else:
            # Data will we sustained

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.number_plate_title = QtWidgets.QLabel(self.centralwidget)
        self.number_plate_title.setGeometry(QtCore.QRect(50, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.number_plate_title.setFont(font)
        self.number_plate_title.setObjectName("number_plate_title")
        self.body_type_title = QtWidgets.QLabel(self.centralwidget)
        self.body_type_title.setGeometry(QtCore.QRect(50, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.body_type_title.setFont(font)
        self.body_type_title.setObjectName("body_type_title")
        self.save_record = QtWidgets.QPushButton(self.centralwidget)
        self.save_record.setGeometry(QtCore.QRect(200, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_record.setFont(font)
        self.save_record.setObjectName("save_record")
        self.save_record.clicked.connect(self.save_vehicle_records)
        self.exempt_vehicle = QtWidgets.QPushButton(self.centralwidget)
        self.exempt_vehicle.setGeometry(QtCore.QRect(200, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.exempt_vehicle.setFont(font)
        self.exempt_vehicle.setObjectName("exempt_vehicle")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(200, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.select_image = QtWidgets.QPushButton(self.centralwidget)
        self.select_image.setGeometry(QtCore.QRect(480, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.select_image.setFont(font)
        self.select_image.setObjectName("select_image")
        self.vehicle_image = QtWidgets.QWidget(self.centralwidget)
        self.vehicle_image.setGeometry(QtCore.QRect(390, 110, 291, 181))
        self.vehicle_image.setTabletTracking(False)
        self.vehicle_image.setAutoFillBackground(False)
        self.vehicle_image.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.vehicle_image.setObjectName("vehicle_image")
        self.number_plate_input = QtWidgets.QLineEdit(self.centralwidget)
        self.number_plate_input.setGeometry(QtCore.QRect(200, 110, 121, 20))
        self.number_plate_input.setObjectName("number_plate_input")
        self.number_plate_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.number_plate_input_2.setGeometry(QtCore.QRect(200, 150, 121, 20))
        self.number_plate_input_2.setObjectName("number_plate_input_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tool Booth Operator Window"))
        self.number_plate_title.setText(_translate("MainWindow", "Vehicle Number Plate"))
        self.body_type_title.setText(_translate("MainWindow", "Vehicle Body Type"))
        self.save_record.setText(_translate("MainWindow", "Save Record"))
        self.exempt_vehicle.setText(_translate("MainWindow", "Exempt Vehicle"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.select_image.setText(_translate("MainWindow", "Select Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
