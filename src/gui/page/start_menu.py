'''
Start menu for the IoT Network Prediction application.
'''

import customtkinter as ctk
import tkinter as tk

from customtkinter import *
from tkinter import *
from src.gui.components.button import CustomButton

class StartMenu(CTkFrame):
  def __init__(self, parent):
    '''
    Initialize the StartMenu frame.

    Parameters:
    - parent: The parent widget (usually the main application window).
    - controller: The controller object to manage navigation between frames.
    '''
    super().__init__(parent)

    # Set the appearance mode and color theme
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    # Create a label for the title
    self.title_label = CTkLabel(self, text="Welcome to IoT Network Prediction", font=("Poppins", 24, "bold"))
    self.title_label.pack(pady=20)

    # Create a button to start the prediction process
    self.start_button = CustomButton(self, text="Start", command=CustomButton.on_button_click)