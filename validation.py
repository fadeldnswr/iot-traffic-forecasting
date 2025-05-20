'''
Validation script to evaluate the performance of the trained models
on the test set. The script loads the preprocessor and the trained models,
compares the forecasted values with the ground truth, and calculates
the Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and
Mean Absolute Error (MAE) for each target column.

Columns: 
- temperature
- humidity(%)
- latency(ms)
- rssi(dBm)
'''

import sys
from typing import List

from src.utils.utils import model_results_error
from src.exception.exception import CustomException

# Define the path to the artifacts directory
esp32_file_path: List[str] = ["esp32_1", "esp32_2"]

if __name__ == "__main__":
  try:
    for list in esp32_file_path:
      # Call the function to print the errors of the model
      print(model_results_error(list))
  except Exception as e:
    raise CustomException(e, sys)