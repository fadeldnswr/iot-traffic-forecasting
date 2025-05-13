'''
Guide page for the Streamlit application.
This page provides an overview of the project, including its objectives, methodology, and expected outcomes.
'''

import streamlit as st

from src.utils.utils import change_page

st.title("GUI Guide")
st.markdown(
    """
    Guide page for the Streamlit application.
    This page provides an overview of the project, including its objectives, methodology, and expected outcomes.
    """
)

# Call the change page function
change_page()