'''
Start menu page for the IoT 
Network Prediction application.
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

    # Create a label for sidebar
    self.title_label = CTkLabel(self, text="", font=("Poppins", 24, "bold"))
    self.title_label.place(relx=0.03, rely=0.5, anchor="w")
    self.title_label.configure(fg_color="#ffffff", width=400, height=950, corner_radius=10)
    
    # Create label for the text inside the sidebar
    self.sidebar_label = CTkLabel(self.title_label, text="Main Menu", font=("Poppins", 30, "bold"))
    self.sidebar_label.place(relx=0.5, rely=0.33, anchor="center")
    
    # Create buttons for the sidebar
    self.start_button = CustomButton(self.title_label, text="Start")
    self.start_button.place(relx=0.5, rely=0.4, anchor="center")
    self.exit_button = CustomButton(self.title_label, text="Exit")
    self.exit_button.place(relx=0.5, rely=0.47, anchor="center")
    
    # Create a label for the main content area
    self.content_label = CTkLabel(self, text="")
    self.content_label.configure(fg_color="#ffffff", width=1200, height=950, corner_radius=10)
    self.content_label.place(relx=0.63, rely=0.5, anchor="center")
    
    # Create a label for the text inside the main content area
    self.content_area_label = CTkLabel(self.content_label, text="Internet of Things Network\nPrediction using ARIMA", font=("Poppins", 70, "bold"))
    self.content_area_label.place(relx=0.5, rely=0.5, anchor="center")