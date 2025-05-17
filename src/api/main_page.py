'''
Welcome page for the API.
This page provides information about the API, including its purpose, usage, and available endpoints.
'''

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def home_page():
  try:
    # Welcome message
    message = "This is the home page of the IoT Network Forecasting Web App API. "
    return {"message": message}
  except Exception as e:
    raise HTTPException(status_code=500, detail=(e))