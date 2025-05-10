'''
Main menu components for
the IoT forecasting project
Graphical User Interface
'''
from gui.constant.constant import BACKGROUND_IMAGE
from PyQt5.QtWidgets import QMainWindow, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

class MainMenu(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Internet of Things Traffic Prediction")
    self.setGeometry(100, 100, 700, 400)
    self.initUI()
  
  def initUI(self):
    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)
    
    layout = QVBoxLayout(central_widget)
    
    # Set the main screen background
    label = QLabel(self)
    pixmap = QPixmap(BACKGROUND_IMAGE)
    label.setPixmap(pixmap)
    label.setScaledContents(True)
    label.setGeometry(0, 0, 1920, 1080)
    
    layout.addWidget(label)
    
    self.button = QPushButton("Start", self)
    self.button.setGeometry(150, 200, 200, 100)
    self.button.setStyleSheet("font-size: 30x; font-family: Poppins; border-radius:5px;")
    self.button.clicked.connect(self.on_click)
    
    layout.addWidget(self.button)
  
  def on_click(self):
    print("Button has been clicked!")
    self.button.setText("Clicked")