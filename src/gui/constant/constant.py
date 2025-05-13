'''
This file is to store the 
file path for every components
as a constant
'''

BACKGROUND_IMAGE = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/src/gui/resources/Main Menu Background.png"
CAPTION_TITLE = """This project focuses on predicting traffic patterns using IoT data and advanced machine learning techniques, 
  ARIMA (AutoRegressive Integrated Moving Average) and LSTM (Long Short-Term Memory). 
  The goal is to forecast traffic conditions in real-time, providing valuable insights for urban planning, traffic management, and optimization.
  """

INTRODUCTION_PAGE = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/src/gui/page/start_menu.py"
ESP32_PAGE_PATH = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/src/gui/page/esp32.py"
GUI_GUIDE_PAGE_PATH = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/src/gui/page/gui_guide.py"

IOT_ARCHITECTURE_CAPTION = """
  The Internet of Things (IoT) architecture for this project consists of three main components:
  1. **ESP32 Microcontroller**: This device acts as a client, collects real-time traffic data from various sensors, such as cameras and ultrasonic sensors.
  It processes the data locally and sends it to the cloud for further analysis.
  2. **Raspberry Pi 4B**: This device acts as a gateway, receiving data from the ESP32 and exporting it into CSV file format.
  It uses the MQTT protocol for communication, ensuring efficient data transfer from ESP32.
  3. **DHT22 Sensor**: This sensor measures temperature and humidity, providing additional context for traffic conditions.
"""
IOT_ARCHITECTURE_PATH = "C:/Kuliah/Semester 6/Signal Processing and Multimedia Services/Project/pslm-project/src/gui/resources/Iot-Architecture.png"

MODEL_CAPTION = """
  The project employs two advanced machine learning models for traffic prediction:
  1. **ARIMA (AutoRegressive Integrated Moving Average)**: A statistical model used for time series forecasting, particularly effective for univariate data.
  2. **LSTM (Long Short-Term Memory)**: A type of recurrent neural network (RNN) designed to learn long-term dependencies, making it suitable for complex time series data.
"""