'''
Custom button components class
'''

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor

class CustomButton(QPushButton):
  def __init__(self, text, parent=None):
    super().__init__(text, parent)
    self.initButton()
  
  def initButton(self):
    self.setStyleSheet("""
      font-family: Poppins;
      font-weight: bold;
      font-size: 18px;
      border-radius: 5px;
      background-color : #9e9e9e;
      
  """)
    self.setGeometry(0, 0, 700, 400)