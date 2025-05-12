'''
Custom button component for the GUI.
This button is a subclass of the CTkButton class from the customtkinter library.
'''

from customtkinter import CTkButton

class CustomButton(CTkButton):
  '''
  Custom button class that inherits from CTkButton.
  This class can be used to create buttons with custom styles and behaviors.
  '''
  def __init__(self, *args, **kwargs):
    '''
    Initialize the custom button with the given arguments.
    
    Parameters:
    - *args: Positional arguments to be passed to the CTkButton constructor.
    - **kwargs: Keyword arguments to be passed to the CTkButton constructor.
    '''
    super().__init__(*args, **kwargs)
    
    # Set the default color theme
    self.configure(fg_color="#00a6ff", hover_color="#53b7ed", text_color="white")
    
    # Set the default font
    self.configure(font=("Poppins", 18, "bold"))
    
    # Set the default size
    self.configure(width=300, height=45)
  
  def on_button_click():
    '''
    Handle the button click event.
    
    This method can be overridden in subclasses to provide custom behavior
    when the button is clicked.
    '''
    print("Button clicked!")