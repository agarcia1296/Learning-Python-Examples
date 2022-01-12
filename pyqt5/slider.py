from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSlider, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Loading the UI File with uic module
        uic.loadUi('slider.ui', self)
        
        # finding the widgets
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.label = self.findChild(QLabel, "label")
        
        # do Something
        self.slider.valueChanged.connect(self.changed_slider)
        
    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))
        
        
app = QApplication([])
window = UI()
window.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")
