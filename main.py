'''
Main GUI application using the
dashh plotly framework.
'''

import sys

from dash import Dash, dcc, html
from src.gui.constant.constant import CAPTION_TITLE
from src.exception.exception import CustomException

# Initialize the Dash application
app = Dash()

# Set the application layout
app.layout = [
  html.H1(children="Welcome to the first Dash Application", style={"textAlign": "center"}),
  html.Div(children=dcc.Markdown(CAPTION_TITLE, 
    style={"textAlign": "justify", "fontSize": 18, "width": "500px", "margin": "auto"}), 
    style={"textAlign": "center"}),
]

if __name__ == "__main__":
  try:
    app.run(debug=True, port=8000)
  except Exception as e:
    raise CustomException(e, sys)