'''
Main backend application for the web app.
The backend is responsible for handling requests, processing data, and returning responses.
The backend is built using FastAPI and is designed to be modular and scalable.
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import graphs, prediction

# Configure the FastAPI application
app = FastAPI(
  title="IoT Network Forecasting Web App",
  description="API for the IoT Network Forecasting Web Application. This API provides endpoints for graphs and prediction.",
  version="1.0.0",
  debug=True
)

# Configure CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Create the routers
app.include_router(graphs.router, tags=["graphs"], prefix="/graphs")
app.include_router(prediction.router, tags=["prediction"], prefix="/prediction")

# Create main page
@app.get("/")
async def main_page():
  return {"message": "Welcome to the IoT Network Forecasting Web App API!"}