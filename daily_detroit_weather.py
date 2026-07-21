# Imports
import logging
import requests
import API_Data_Collection

# Setup the basic logging configuration
logging.basicConfig(
    filename="daily_detroit.log", 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# URL and User agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

data = API_Data_Collection.get_weather_info("detroit", headers, 8)
API_Data_Collection.print_weather_report("detroit", data)