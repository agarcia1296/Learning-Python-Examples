from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QSlider, QLabel, QLineEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QDialog):
    def __init__(self):
        super().__init__()
        
        #Loading the UI File with uic module
        uic.loadUi('login_demo.ui', self)
        
        # finding the widgets
        self.title_label = self.findChild(QLabel, "title_label")
        self.username_label = self.findChild(QLabel, "username_label")
        self.password_label = self.findChild(QLabel, "password_label")
        self.username_lineEdit = self.findChild(QLineEdit, "username_lineEdit")
        self.password_lineEdit = self.findChild(QLineEdit, "password_lineEdit")
        self.login_pushButton = self.findChild(QPushButton, "login_pushButton")
        
        
        
        # do Something
        #self.slider.valueChanged.connect(self.changed_slider)

        
        
app = QApplication([])
window = UI()
window.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")