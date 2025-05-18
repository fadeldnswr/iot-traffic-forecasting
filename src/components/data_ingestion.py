'''
This module contains the DataIngestion class, which is responsible for
ingesting data from various sources, including CSV files and databases.
'''

import os
import sys
import pandas as pd

from src.exception.exception import CustomException
from src.logging.logging import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class DataIngestionConfig:
  '''
  Configuration to store the train, test, and raw data
  into artifacts folder.
  '''
  def __init__(self, device_id: str):
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    data_dir = os.path.join(PROJECT_ROOT, "data", device_id)
    self.raw_data_path = os.path.join(data_dir, "raw_data.csv")
    self.train_data_path = os.path.join(data_dir, "train_data.csv")
    self.test_data_path = os.path.join(data_dir, "test_data.csv")
    self.source_path = os.path.join(PROJECT_ROOT, "data", f"{device_id}.csv")

class DataIngestion:
  '''
  Process of collecting and importing data from various sources
  into central location, such as database or data warehouse, for storage,
  processing, and analysis.
  '''
  def __init__(self, device_id: str):
    self.device_id = device_id
    self.ingestion_config = DataIngestionConfig(device_id=self.device_id)
  
  def initiate_data_ingestion(self):
    '''
    Function to create data ingestion pipeline. In this case,
    the dataset is being retrieved from another folder. Usually, this function
    is going to retrieve the data from the database or API.
    '''
    logging.info(f"Starting data ingestion for {self.device_id}")
    try:
      # Read the dataset from the CSV file
      df = pd.read_csv(self.ingestion_config.source_path)
      logging.info(f"Read the dataset as dataframe")
      
      # Make the directory for the artifacts folder
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
      
      # Save the raw dataset
      df.to_csv(self.ingestion_config.raw_data_path, index=False)
      logging.info(f"Saved the raw dataset to {self.ingestion_config.raw_data_path}")
      
      # Split the dataset into train and test sets
      logging.info(f"Splitting the dataset into train and test sets")
      train_size = int(0.8 * len(df))
      train_set, test_set = df[:train_size], df[train_size:]
      train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
      test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
      logging.info(f"Data ingestion completed successfully")
      
      # Return the train and test sets
      return (
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )
    except Exception as e:
      raise CustomException(e, sys)

# Define esp32 file path
esp32_1_file_path = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/data/esp32_1_data.csv"
esp32_2_file_path = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/data/esp32_2_data.csv"

# Read the dataset
df_esp32_1 = pd.read_csv(esp32_1_file_path)
df_esp32_2 = pd.read_csv(esp32_2_file_path)

# Initialize the main application
if __name__ == "__main__":
  try:
    # Initialize the data ingestion
    ingestion = DataIngestion(device_id=f"esp32_2_data")
    train_path, test_path = ingestion.initiate_data_ingestion()
    
    # Load the train and test data
    df_train = pd.read_csv(train_path)
    
    # Define the target column
    target_column = ["temperature", "humidity(%)", "latency(ms)", "packet_loss(%)", "throughput(bytes/sec)", "rssi(dBm)"]
    
    # Data transformation
    data_transform = DataTransformation(
      df=df_train.copy(),
      time_column="timestamp",
      target_column=None,
      device_id="esp32_2",
    )
    data_transform.get_data_transformer_object()
    data_transform.save_for_visualization()
    
    for col in target_column:
      print(f"Training model for {col}")
      data_transform.target_column = col
      series = data_transform.get_series()
      train_series, test_series, _, _ = data_transform.initiate_data_transformation()
      
      # Train the ARIMA model
      model_trainer = ModelTrainer(series=train_series, order=(1, 1, 1), model_name=f"esp32_2_{col}")
      mse = model_trainer.initiate_model_trainer()
  except Exception as e:
    raise CustomException(e, sys)