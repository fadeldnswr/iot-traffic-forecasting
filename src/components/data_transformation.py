'''
This module contains the DataTransformation class, which is responsible for
transforming data for machine learning models.
It includes methods for encoding categorical features, scaling numerical features,
'''

import sys
import os
import pandas as pd

from dataclasses import dataclass
from src.exception.exception import CustomException
from src.logging.logging import logging
from src.utils.utils import save_object

@dataclass
class DataTransformationConfig:
  '''
  Configuration class to store the transformed
  data into the artifacts folder.
  '''
  preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
  def __init__(self, df: pd.DataFrame, time_column: str, target_column: str):
    self.data_transformation_config = DataTransformationConfig()
    self.time_column = time_column
    self.target_column = target_column
    self.df = df
    self.series = None
  
  def get_data_transformer_object(self) -> pd.Series:
    '''
    The function is responsible for data transformation
    based on the feature of the dataset.
    '''
    try:
      # Convert time column to datetime
      self.df[self.time_column] = pd.to_datetime(self.df[self.time_column], format="%Y-%m-%d | %H:%M:%S")
      logging.info(f"Converted {self.time_column} to datetime")
      
      # Set the time column as the index
      self.df.set_index(self.time_column, inplace=True)
      logging.info(f"The {self.time_column} set as an index")
      
      # Resample the data to 1 minute intervals
      self.df = self.df.resample("min").mean()
      logging.info(f"Dataset shape after resampling: {self.df.shape}")
      logging.info(f"Null values in the dataset\n{self.df.isnull().sum()}")
      
      # Imputate the missing values
      self.df.fillna(self.df.mean(), inplace=True)
      logging.info(f"Null values in the dataset\n{self.df.isnull().sum()}")
      
      # Show the data for 24 hours
      self.series = self.df.loc["2025-05-12 12:00:00":"2025-05-13 12:00:00", self.target_column]
      logging.info(f"Dataset for 24 hours: {self.series.shape}")
      return self.series
    except Exception as e:
      raise CustomException(e, sys)
  
  def initiate_data_transformation(self) -> pd.Series:
    '''
    The function is responsible for data transformation
    based on the feature of the dataset.
    '''
    try:
      if self.series is None:
        raise CustomException("Data series is not set. Please call get_data_transformer_object() first.")
      logging.info("Data transformation started")
      
      # Create differencing series
      series_diff_data = self.series.diff().dropna()
      logging.info("Differencing series created")
      
      # Split into train and test data
      train_size = int(len(self.series) * 0.8)
      train = series_diff_data[:train_size]
      test = series_diff_data[train_size:]
      logging.info(f"Applying preprocessing object on training and test dataframe")
      
      # Save the preprocessor object
      save_object(
        file_path=self.data_transformation_config.preprocessor_obj_file_path,
        obj=self.series
      )
      
      return (
        train,
        test,
        self.data_transformation_config.preprocessor_obj_file_path,
      )
    except Exception as e:
      raise CustomException(e, sys)