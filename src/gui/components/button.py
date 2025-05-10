'''
Custom button components class
for the GUI
'''

from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect

class CustomButton(QPushButton):
  def __init__(self, text, parent=None):
    super().__init__(text, parent)
    self.initButton()
  
  def initButton(self):
    # Create button's drop shadow
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(10)
    
    self.setStyleSheet("""
      font-family: Poppins;
      font-weight: bold;
      font-size: 18px;
      border-radius: 11px;
      background-color : #ffffff;
      padding: 15px 30px;
  """)
    self.setGraphicsEffect(shadow)