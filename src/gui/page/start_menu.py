'''
This file is for the introductory page of the GUI.
It provides an overview of the project, including its objectives, methodology, and expected outcomes.
''' 

import streamlit as st
from src.gui.constant.constant import CAPTION_TITLE

st.title("Project Introduction")
st.markdown(CAPTION_TITLE)