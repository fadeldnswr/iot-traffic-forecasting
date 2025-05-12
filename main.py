'''
Main GUI application using the
Streamlit library.
'''

import streamlit as st
import pandas as pd

from src.gui.constant.constant import (
  CAPTION_TITLE, INTRODUCTION_PAGE, 
  ESP32_PAGE_PATH, GUI_GUIDE_PAGE_PATH)

# Define the pages
project_introduction = st.Page(INTRODUCTION_PAGE, title="Project Introduction")
gui_guide = st.Page(GUI_GUIDE_PAGE_PATH, title="GUI Guide")
esp32_page = st.Page(ESP32_PAGE_PATH, title="Choose ESP32 Device")

pages = {
  "Overview": [project_introduction, gui_guide],
  "Project": [esp32_page]
}

pg = st.navigation(pages)
pg.run()