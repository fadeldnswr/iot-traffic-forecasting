'''
Main GUI application using the
combination of CustomTkinter and Tkinter.
'''

import customtkinter as ctk
import tkinter as tk

from customtkinter import *
from tkinter import *
from src.gui.components.button import CustomButton
from src.gui.page.start_menu import StartMenu

# Initialize the main application
app = CTk()

# Initialize the StartMenu frame
start_menu = StartMenu(app)
start_menu.pack(fill="both", expand=True)

# Create label
app.mainloop()