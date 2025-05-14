'''
Utility functions for the project.
These functions are used to perform various tasks such as data processing,
visualization, and machine learning model training.
The functions are designed to be reusable and modular, allowing for easy integration into the main application.
'''

import pandas as pd
import sys
import matplotlib.pyplot as plt

from typing import List, Tuple
from src.exception.exception import CustomException

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

# Check the data type of a column function
def check_data_type(df:pd.DataFrame)-> None:
  '''
  Check the data type of each column in a DataFrame.
  Parameters:
  df (pd.DataFrame): The DataFrame to check.
  '''
  try:
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
      raise ValueError("The input is not a DataFrame.")
    # Check if the DataFrame is empty
    if df.empty:
      raise ValueError("The DataFrame is empty.")
    for col in df.columns:
      print(f"Column: {col}\nData Type: {df[col].dtype}\n")
  except Exception as e:
    raise CustomException(e, sys)

# Create stationarity check function 
def check_stationarity(data):
  """
  Check if the time series data is stationary using the Augmented Dickey-Fuller test.
  Parameters:
  data (pd.Series): The time series data to check.
  Returns:
  bool: True if the data is stationary, False otherwise.
  """
  result = adfuller(data, autolag="AIC")
  
  # Define Result Variable
  adf_stats = result[0]
  p_value = result[1]
  used_lags = result[2]
  critical_value = result[4]
  
  # Print values
  print(f"ADF Statistics : {adf_stats}")
  print(f"P-Value : {p_value}")
  print(f"Used Lags : {used_lags}")
  print(f"Critical Value : {critical_value}")
  
  # Check if P-Value less than 0.05
  if p_value < 0.05:
    print("The data is stationer (Reject H0)")
  else:
    print("The data is not stationer (Failed to reject H0)")
  
  # Return value
  return [adf_stats, p_value, used_lags, critical_value]

# Create the function to plot the ACF and PACF
def plot_acf_pacf(data: pd.DataFrame, lags:int, title:str):
  '''
  Plot the ACF and PACF of the time series data.
  Parameters:
  data (pd.DataFrame): The time series data to plot.
  lags (int): The number of lags to plot.
  '''
  try:
    fig, ax = plt.subplots(1, 2, figsize=(8, 5))
    
    # Plot the ACF
    plot_acf(data, lags=lags, ax=ax[0])
    ax[0].set_title(f'(ACF) for {title}', fontsize=9)
    ax[0].set_xlabel('Lags')
    ax[0].set_ylabel('ACF')
    
    # Plot the PACF
    plot_pacf(data, lags=lags, ax=ax[1])
    ax[1].set_title(f'(PACF) for {title}', fontsize=9)
    ax[1].set_xlabel('Lags')
    ax[1].set_ylabel('PACF')

    plt.tight_layout()
    plt.show()
  except Exception as e:
    raise CustomException(e, sys)