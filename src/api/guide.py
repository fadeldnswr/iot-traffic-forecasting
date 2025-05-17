'''
This is the guide page for the API.
This page provides information about the API, including its purpose, usage, and available endpoints.
'''

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def guide_page():
  try:
    # Welcome message
    message = "This is the guide page of the IoT Network Forecasting Web App API. "
    return {"message": message}
  except Exception as e:
    raise HTTPException(status_code=500, detail=(e))