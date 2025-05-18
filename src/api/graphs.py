'''
This api page for the graphs.
This page provides information about the graphs, including its purpose, usage, and available endpoints.
'''

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from src.utils.utils import load_object

import os
import pandas as pd

router = APIRouter()

# Define the path to the model
PROCESSED_DATA_PATH = "artifacts/preprocessor.pkl"

# Path parameters for all the graphs
@router.get("/all", 
  summary="Get all the graphs for the processed data", 
  description="This endpoint returns all the graphs for the processed data.")
async def all_graphs_page():
  try:
    # Check if the processed data file exists
    if not os.path.exists(PROCESSED_DATA_PATH):
      return JSONResponse(status_code=400, content={
        "error": "Processed data file not found."
      })
    
    # Load the processed data
    df: pd.DataFrame = load_object(PROCESSED_DATA_PATH)
    print(df.head())
    
    # Prepare the data for plotting
    timestamps = df.index.strftime("%Y-%m-%d %H:%M").tolist()
    data = {col: df[col].tolist() for col in df.columns}
    
    # Return the data as JSON
    return JSONResponse(
      status_code=200, content={
        "labels": timestamps,
        "data": data
      }
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

# Query parameters for the popup graphs
@router.get("/",
  summary="Get the graphs for the processed data based on the query parameters",
  description="This endpoint returns the graphs for the processed data based on the query parameters for the popup graphs.")
async def graphs_page(columns: str = Query(..., description="Comma-separated list of columns to plot")):
  try:
    # Check if the processed data file exists
    if not os.path.exists(PROCESSED_DATA_PATH):
      return JSONResponse(status_code=404, content={
        "error": "Processed data file not found."
      })
    
    # Load the processed data
    df: pd.DataFrame = load_object(PROCESSED_DATA_PATH)
    print(df.head())
    
    # Check if the columns exist in the DataFrame
    requested_cols = columns.split(",")
    missing_cols = [col for col in requested_cols if col not in df.columns]
    if missing_cols:
      return JSONResponse(status_code=404, content={
        "error": f"Columns not found: {', '.join(missing_cols)}"
      })
    
    # Prepare the data for plotting
    timestamps = df.index.strftime("%Y-%m-%d %H:%M").tolist()
    data = {col: df[col].tolist() for col in requested_cols}
    
    return JSONResponse(status_code=200, content={
      "labels": timestamps,
      "data": data
    })
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))