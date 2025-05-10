import sys
import os

# Menambahkan path folder src ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from PyQt5.QtWidgets import QApplication

from src.exception.exception import CustomException
from src.logging.logging import logging
from gui.page.start_menu import MainMenu

# Main Function to run the application
def main_screen():
  app = QApplication(sys.argv)
  window = MainMenu()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  try:
    main_screen()
  except Exception as e:
    raise CustomException(e, sys)