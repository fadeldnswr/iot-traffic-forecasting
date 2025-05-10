'''
Main menu components for
the IoT forecasting project
Graphical User Interface
'''
from gui.constant.constant import BACKGROUND_IMAGE
from gui.components.button import CustomButton

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internet of Things Traffic Prediction")
        self.setGeometry(100, 100, 1920, 1080)
        self.initUI()

    def initUI(self):
        # Create central widget
        self.central_widget = QWidget(self)
        
        # Create image label
        self.image_label = QLabel(self.central_widget)
        self.image_label.setGeometry(QRect(-1, -21, 1920, 1080))
        pixmap = QPixmap(BACKGROUND_IMAGE)
        self.image_label.setPixmap(pixmap)
        
        # Create and config the title
        self.title = QLabel("Internet of Things Traffic Prediction with ARIMA and LSTM", self.central_widget)
        self.title.setGeometry(QRect(180, 180, 1551, 644))
        
        # Create custom font for title and button
        font = QFont()
        font.setFamily("Poppins")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        
        # Configure title font
        self.title.setFont(font)
        self.title.setStyleSheet("color: white;")
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        
        # Configure button font
        self.start_button = CustomButton("Start", self.central_widget)
        self.start_button.setGeometry(QRect(800, 700, 291, 50))
        self.start_button.setFont(font)
        self.setCentralWidget(self.central_widget)
