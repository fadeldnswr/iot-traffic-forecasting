'''
This module contains the ARIMA model training class,
which is responsible for training the ARIMA model
on the time series data.
'''

import os
import pandas as pd
import sys

from dataclasses import dataclass
from src.exception.exception import CustomException
from src.logging.logging import logging
from src.utils.utils import save_object

from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

@dataclass
class ModelTrainerConfig:
  '''
  Configuration class to store the model
  training artifacts.
  '''
  def __init__(self, model_name: str):
    self.trained_model_file_path = os.path.join("artifacts", f"{model_name}_model.pkl")

class ModelTrainer:
  '''
  Class to train the ARIMA model on the time series data.
  '''
  def __init__(self, series: pd.Series, order=(1, 1, 1), model_name: str = "model"):
    self.model_trainer_config = ModelTrainerConfig(model_name=model_name)
    self.series = series
    self.model = None
    self.order = order
  
  def initiate_model_trainer(self):
    try:
      # Split the data into train and test sets
      logging.info(f"Splitting the data into train and test sets")
      train_size = int(0.8 * len(self.series))
      train_set, test_set = self.series[:train_size], self.series[train_size:]
      logging.info(f"Train set shape: {train_set.shape}") # Shape of the train set
      logging.info(f"Test set shape: {test_set.shape}") # Shape of the test set
      
      # Train the ARIMA model
      logging.info(f"Training the ARIMA model")
      model = ARIMA(train_set, order=self.order).fit()
      
      # Forecast 
      forecast = model.forecast(steps=len(test_set))
      
      # Evaluate the model
      mse = mean_squared_error(test_set, forecast)
      logging.info(f"Mean Squared Error: {mse}")
      
      # Save the model
      os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
      save_object(self.model_trainer_config.trained_model_file_path, model, device_id=self.model_trainer_config.trained_model_file_path)
      logging.info(f"Model saved to {self.model_trainer_config.trained_model_file_path}")
      
      return mse
    except Exception as e:
      raise CustomException(e, sys)