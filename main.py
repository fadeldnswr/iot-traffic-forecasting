'''
Main GUI application using the
Streamlit library.
'''

import streamlit as st
import sys

from src.gui.constant.constant import (
  INTRODUCTION_PAGE, ESP32_PAGE_PATH, 
  GUI_GUIDE_PAGE_PATH
  )

from src.exception.exception import CustomException
from src.logging.logging import logging

# Define the pages
# ===============================

# To make the pages inside the navigation bar, 
# we need to define the pages as a list of tuples.
# The first element of the tuple is the page name,
# and the second element is the page object.

project_introduction = st.Page(INTRODUCTION_PAGE, title="Project Introduction")
gui_guide = st.Page(GUI_GUIDE_PAGE_PATH, title="GUI Guide")
esp32_page = st.Page(ESP32_PAGE_PATH, title="ESP32 Exploratory Data Analysis")

pages = {
  "Overview": [project_introduction, gui_guide],
  "Project": [esp32_page]
}

if __name__ == "__main__":
  try:
    logging.info("Starting the Streamlit application")
    st.set_page_config(
      page_title="Internet of Things Traffic Prediction",
      page_icon="🚦",
      initial_sidebar_state="expanded"
    )
    pg = st.navigation(pages)
    pg.run()
  except Exception as e:
    st.exception(CustomException(e, sys))