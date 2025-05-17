'''
This api page for the graphs.
This page provides information about the graphs, including its purpose, usage, and available endpoints.
'''

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def graphs_page():
  try:
    # Welcome message
    message = "This is the graphs page of the IoT Network Forecasting Web App API. "
    return {"message": message}
  except Exception as e:
    raise HTTPException(status_code=500, detail=(e))