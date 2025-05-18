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
PROCESSED_DATA_PATH = os.path.join(MODEL_BASE_PATH, "preprocessor.pkl")

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

# Define endpoint for the POST request
@router.post("/",
  summary="Predict the target variable for a specific hour",
  description="This endpoint predicts the target variable for a specific hour.",
  )
async def predict_hour(
  columns: str = Query(..., description="Target column to predict"), 
  hour: int = Query(..., ge=1, le=10, description="Hour to predict")):
  try:
    # Check if the processed data file exists
    if not os.path.exists(PROCESSED_DATA_PATH):
      return JSONResponse(status_code=400, content={
        "error": "Processed data file not found."
      })
    
    # Load the processed data
    df: pd.DataFrame = load_object(PROCESSED_DATA_PATH)
    if columns not in df.columns:
      return JSONResponse(status_code=400, content={
        "error": f"Column {columns} not found in the processed data."
      })
    
    # Load the model
    model_path = os.path.join(MODEL_BASE_PATH, f"esp32_1_{columns}_model.pkl")
    if not os.path.exists(model_path):
      return JSONResponse(status_code=400, content={
        "error": f"Model for {columns} not found."
      })
    model: ARIMAResults = load_object(model_path)
    steps = hour * 60 # Convert hours to minutes
    prediction = model.forecast(steps=steps)
    
    last_value = df[columns].iloc[-1]
    prediction_restored = prediction.cumsum() + last_value
    future_index = pd.date_range(start=df.index[-1] + pd.Timedelta(minutes=1), periods=steps, freq="min")
    
    return JSONResponse(status_code=200, content={
      "labels": future_index.strftime("%Y-%m-%d %H:%M").tolist(),
      "data": prediction_restored.tolist()
    })
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))