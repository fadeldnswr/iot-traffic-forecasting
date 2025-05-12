'''
This file is for the ESP32 page of the GUI.
It allows the user to select an ESP32 device from a list of available devices.
'''

import streamlit as st

st.title("ESP32 Device Selection")
st.markdown(
    """
    ## Choose ESP32 Device
    Please select the ESP32 device you want to use for traffic prediction.
    """
)