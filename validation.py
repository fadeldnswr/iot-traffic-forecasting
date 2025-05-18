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

import pandas as pd
import numpy as np
import dill

from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load data dan model
with open("artifacts/preprocessor.pkl", "rb") as f:
  df = dill.load(f)

# Define the target columns and metrics
target_column = ["temperature", "humidity(%)", "latency(ms)", "rssi(dBm)"]
metrics = []

for col in target_column:
  with open(f"artifacts/esp32_1_{col}_model.pkl", "rb") as f:
    model = dill.load(f)
  
  # Dapatkan nilai terakhir
  last_value = df[col].iloc[-1]
  
  # Forecast 288 langkah (5 jam)
  steps = 288
  forecast = model.forecast(steps=steps)
  forecast_restored = forecast.cumsum() + last_value
  
  # Ground truth
  ground_truth = df[col].iloc[-steps:]
  
  # Hitung MSE
  mse = mean_squared_error(ground_truth, forecast_restored)
  rmse = np.sqrt(mse)
  mae = mean_absolute_error(ground_truth, forecast_restored)
  
  # Save the errors in dataframe format
  metrics.append({
    "Column": col,
    "mse": mse,
    "rmse": rmse,
    "mae": mae
  })

# Print the results
results = pd.DataFrame(metrics)
print(results)