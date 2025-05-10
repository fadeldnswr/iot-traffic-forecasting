'''
Main menu components for
the IoT forecasting project
Graphical User Interface
'''
from gui.constant.constant import BACKGROUND_IMAGE
from gui.components.button import CustomButton

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

class MainMenu(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Internet of Things Traffic Prediction")
    self.setGeometry(100, 100, 700, 400)
    self.initUI()
  
  def initUI(self):
    # Set the central widget
    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)
    
    # Create horizontal layout
    main_layout = QHBoxLayout(central_widget)
    
    # Set the left panel layout
    left_panel_layout = QVBoxLayout()
    
    # Create the button
    self.start_button = CustomButton("Start", self)
    self.start_button.clicked.connect(self.on_click)
    
    self.exit_button = CustomButton("Exit", self)
    self.exit_button.clicked.connect(self.on_click)
    
    # Add the left panel button
    left_panel_layout.addWidget(self.start_button)
    left_panel_layout.addWidget(self.exit_button)
    
    # Create label for the background image
    righ_panel_layout = QVBoxLayout()
    label = QLabel(self)
    pixmap = QPixmap(BACKGROUND_IMAGE)
    label.setPixmap(pixmap)
    label.setScaledContents(True)
    
    # Create text label
    text_label = QLabel("Internet of Things Traffic Prediction with ARIMA")
    text_label.setAlignment(Qt.AlignCenter)
    text_label.setStyleSheet("font-size: 24px; font-family: Poppins; font-weight: bold;")
    
    # Add image label into the right panel
    righ_panel_layout.addWidget(label)
    righ_panel_layout.addWidget(text_label)
    
    # Add left and right panel into the main layout
    main_layout.addLayout(left_panel_layout)
    main_layout.addLayout(righ_panel_layout)
  
  def on_click(self):
    print("Button has been clicked!")
    self.start_button.setText("Clicked")