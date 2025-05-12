'''
This file is for the introductory page of the GUI.
It provides an overview of the project, including its objectives, methodology, and expected outcomes.
''' 

import streamlit as st

st.title("Project Introduction")
st.markdown(
    """
    ## Project Overview
    This project focuses on predicting traffic patterns using IoT data and advanced machine learning techniques, 
    ARIMA (AutoRegressive Integrated Moving Average) and LSTM (Long Short-Term Memory). 
    The goal is to forecast traffic conditions in real-time, providing valuable insights for urban planning, traffic management, and optimization.
    
    ## Objectives
    - To develop a robust traffic prediction model using ARIMA and LSTM.
    - To analyze the performance of both models in terms of accuracy and efficiency.
    - To provide a user-friendly interface for real-time traffic prediction.
    
    ## Methodology
    1. Data Collection: Gather IoT data related to traffic patterns.
    2. Data Preprocessing: Clean and prepare the data for analysis.
    3. Model Development: Implement ARIMA and LSTM models for traffic prediction.
    4. Model Evaluation: Compare the performance of both models using appropriate metrics.
    
    ## Expected Outcomes
    - A comprehensive report on the performance of ARIMA and LSTM models.
    - A user-friendly GUI for real-time traffic prediction.
    
    ## Conclusion
    This project aims to enhance traffic management systems by leveraging IoT data and advanced machine learning techniques. 
    The expected outcomes will provide valuable insights for urban planners and traffic managers.
    
    """
)