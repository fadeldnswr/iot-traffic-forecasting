'''
Main GUI application using the
combination of CustomTkinter and Tkinter.
'''

import sys

from customtkinter import *
from tkinter import *
from src.gui.page.start_menu import StartMenu
from src.exception.exception import CustomException
from src.logging.logging import logging

# Initialize the main application
app = CTk()
app.title("Internet of Things Network Prediction")
app.geometry("1920x1080")
app.configure(fg_color="#f0f0f0")

# Initialize the StartMenu frame
start_menu = StartMenu(app)
start_menu.pack(fill="both", expand=True)

# Create label
if __name__ == "__main__":
  try:
    logging.info("Starting the IoT Network Prediction GUI application.")
    app.mainloop()
  except Exception as e:
    raise CustomException(e, sys)