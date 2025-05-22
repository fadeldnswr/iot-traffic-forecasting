'''
Main backend application for the web app.
The backend is responsible for handling requests, processing data, and returning responses.
The backend is built using FastAPI and is designed to be modular and scalable.
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import graphs, esp1_prediction, esp2_prediction

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
app.include_router(esp1_prediction.router, tags=["esp32-1-prediction"], prefix="/esp32-1-prediction")
app.include_router(esp2_prediction.router, tags=["esp32-2-prediction"], prefix="/esp32-2-prediction")

# Create main page
@app.get("/")
async def main_page():
  return {"message": "Welcome to the IoT Network Forecasting Web App API!"}