'''
Main script to run the
Streamlit application.
'''

import streamlit as st
import pandas as pd

st.write("# Welcome to the Streamlit App")
st.write("This is a boilerplate for our Streamlit application.")

# Example of a dataframe
df = pd.DataFrame({
    "Column 1": [1, 2, 3],
    "Column 2": ["A", "B", "C"],
    "Column 3": [4.5, 5.5, 6.5]
})

# Put dataframe in the Streamlit app
st.write("## Example DataFrame")
st.dataframe(df)