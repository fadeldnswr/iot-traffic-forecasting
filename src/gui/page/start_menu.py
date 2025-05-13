'''
This file is for the introductory page of the GUI.
It provides an overview of the project, including its objectives, methodology, and expected outcomes.
''' 

import streamlit as st
from src.gui.constant.constant import (
  CAPTION_TITLE, IOT_ARCHITECTURE_CAPTION,
  IOT_ARCHITECTURE_PATH, MODEL_CAPTION,
)
from src.utils.utils import change_page

# Initialize the page
st.title("Project Introduction")
st.markdown(CAPTION_TITLE)

# Initialize the IoT Architecture section
st.subheader("Internet of Things Architecture")
st.markdown(IOT_ARCHITECTURE_CAPTION)
st.image(IOT_ARCHITECTURE_PATH, caption="Internet of Things Architecture", use_container_width=True)

# Initialize the model section
st.subheader("Time Series Prediction Models")
st.markdown(MODEL_CAPTION)

# Call the change page function
change_page()