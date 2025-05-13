'''
Utility functions for the project.
These functions are used to perform various tasks such as data processing,
visualization, and machine learning model training.
The functions are designed to be reusable and modular, allowing for easy integration into the main application.
'''

import streamlit as st
import sys
from typing import Dict

from src.exception.exception import CustomException
from src.gui.constant.constant import (
  INTRODUCTION_PAGE, ESP32_PAGE_PATH, 
  GUI_GUIDE_PAGE_PATH
)

# Global variables

# ===============================
# List of pages
pages = {
  "Project Introduction": INTRODUCTION_PAGE,
  "GUI Guide": GUI_GUIDE_PAGE_PATH,
  "Choose ESP32 Devices": ESP32_PAGE_PATH,
}

# Change page function
def change_page(pages=pages) -> Dict[str, str]:
  """
  Function to change the page in Streamlit.
  Args:
    pages (str): The name of the page to switch to.
  """
  try:
    # Dropdown to select the page
    selected_page = st.selectbox("Select a page", list(pages.keys()))
    
    # Button to switch page
    _, _, right = st.columns(3)
    if right.button("Switch Page", use_container_width=True):
      # Switch to the selected page
      page_file = pages[selected_page]
      st.switch_page(page_file)
  except Exception as e:
    st.exception(CustomException(e, sys))