'''
This API is responsible for handling the prediction of the
IoT network forecasting web app.
'''

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from src.utils.utils import load_object
from statsmodels.tsa.arima.model import ARIMAResults

import os
import pandas as pd

router = APIRouter()

# Define the path to the model
MODEL_BASE_PATH = "artifacts"
PROCESSED_DATA_PATH = os.path.join(MODEL_BASE_PATH, "esp32_1_preprocessor.pkl")

# Define path parameters for all the predictions graphs
@router.get("/all",
  summary="Get all the predictions for the processed data",
  description="This endpoint returns all the predictions for the processed data.",
  )
async def predict_all():
  '''
  This endpoint is used to predict the target variable
  based on the input data.
  '''
  try:
    # Check if the processed data file exists
    if not os.path.exists(PROCESSED_DATA_PATH):
      return JSONResponse(status_code=400, content={
        "error": "Processed data file not found."
      })
    
    # Load the processed data
    df: pd.DataFrame = load_object(PROCESSED_DATA_PATH)
    predictions = {} # Store predictions for each column
    
    for col in df.columns:
      model_path = os.path.join(MODEL_BASE_PATH, f"esp32_1_{col}_model.pkl")
      if os.path.exists(model_path):
        model: ARIMAResults = load_object(model_path)
        forecast = model.forecast(steps=60) # Default to 60 minutes
        last_value = df[col].iloc[-1]
        forecast = forecast.cumsum() + last_value
        predictions[col] = forecast.tolist()
    
    timestamp = pd.date_range(start=df.index[-1] + pd.Timedelta(minutes=1), periods=60, freq="min")
    return JSONResponse(status_code=200, content={
      "labels": timestamp.strftime("%Y-%m-%d %H:%M").tolist(),
      "data": predictions
    })
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

# Define query parameters for the prediction graphs
@router.get("/",
  summary="Get the predictions for the processed data based on the query parameters",
  description="This endpoint returns the predictions for the processed data based on the query parameters.",
  )
async def predict_popup(columns: str = Query(..., description="Comma-separated list of columns to predict")):
  '''
  This endpoint is used to predict the target variable
  based on the input data.
  '''
  try:
    # Check if the processed data file exists
    if os.path.exists(PROCESSED_DATA_PATH):
      return JSONResponse(status_code=400, content={
        "error": "Processed data file not found."
      })
    
    # Load the processed data
    df: pd.DataFrame = load_object(PROCESSED_DATA_PATH)
    requested_cols = [col.strip() for col in columns.split(",")]
    predictions = {} # Store predictions for each column
    
    # Check if the columns exist in the DataFrame
    for col in requested_cols:
      if col not in df.columns:
        return JSONResponse(status_code=400, content={
          "error": f"Column {col} not found in the processed data."
        })
      
      # Check if the model exists
      model_path = os.path.join(MODEL_BASE_PATH, f"esp32_1_{col}_model.pkl")
      if not os.path.exists(model_path):
        return JSONResponse(status_code=400, content={
          "error": f"Model for {col} not found."
        })
      
      # Load the model and mak predictions
      model: ARIMAResults = load_object(model_path)
      forecast = model.forecast(steps=60) # Default to 60 minutes
      last_value = df[col].iloc[-1]
      forecast = forecast.cumsum() + last_value
      predictions[col] = forecast.tolist() # Store predictions for each column
    timestamp = pd.date_range(start=df.index[-1] + pd.Timedelta(minutes=1), periods=60, freq="min")
    return JSONResponse(status_code=200, content={
      "labels": timestamp.strftime("%Y-%m-%d %H:%M").tolist(),
      "data": predictions
    })
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def predict_all_columns(
  hour: int = Query(..., ge=1, le=10, description="Hour to predict")):
  try:
    if not os.path.exists(PROCESSED_DATA_PATH):
      return JSONResponse(status_code=400, content={"error": "Processed data file not found."})

    df: pd.DataFrame = load_object(PROCESSED_DATA_PATH)
    target_columns = ["temperature", "humidity(%)", "latency(ms)", "packet_loss(%)", "throughput(bytes/sec)", "rssi(dBm)"]
    steps = hour * 60
    predictions = {}
    all_labels = None
    actual_length = 0

    # Ambil 80% terakhir dari data
    split_index = int(len(df) * 0.8)
    df_actual = df.iloc[-split_index:]

    for col in target_columns:
      model_path = os.path.join(MODEL_BASE_PATH, f"esp32_2_{col}_model.pkl")
      if not os.path.exists(model_path):
        continue

      model: ARIMAResults = load_object(model_path)
      forecast = model.forecast(steps=steps)
      last_value = df[col].iloc[-1]
      forecast_restored = forecast.cumsum() + last_value

      # Gabungkan actual dan forecast
      combined = pd.concat([df_actual[col], forecast_restored], ignore_index=True)
      predictions[col] = combined.tolist()

      # Label (timestamp) hanya dibuat sekali
      if all_labels is None:
        actual_timestamps = df_actual.index
        forecast_start = actual_timestamps[-1] + pd.Timedelta(minutes=1)
        forecast_timestamps = pd.date_range(start=forecast_start, periods=steps, freq="min")
        all_labels = list(actual_timestamps.strftime("%Y-%m-%d %H:%M")) + list(forecast_timestamps.strftime("%Y-%m-%d %H:%M"))
        actual_length = len(actual_timestamps)

    return JSONResponse(status_code=200, content={
      "labels": all_labels,
      "data": predictions,
      "actual_length": actual_length
    })
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))