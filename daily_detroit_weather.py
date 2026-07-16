# Imports
import logging
import requests

# Setup the basic logging configuration
logging.basicConfig(filename="daily_detroit.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL and User agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
url = "https://wttr.in/detroit?format=j1"

# Starts try block
try:
    response = requests.get(url, headers=headers)

    # SUCCESS: Checks if status code is 200
    if response.status_code == 200:
        data = response.json()
        current_weather = data["current_condition"][0]
        nearest_area = data["nearest_area"][0]

        temp = current_weather["temp_F"]
        feel_temp = current_weather["FeelsLikeF"]
        humid = current_weather["humidity"]
        uv = current_weather["uvIndex"]
        wind_dir = current_weather["winddir16Point"]
        wind_speed = current_weather["windspeedMiles"]
        region_val = nearest_area["region"][0]["value"]

        # LOG SUCCESS
        logging.info(
            f"SUCCESS - City: Detroit | Region: {region_val} | Temp: {temp}F | FeelsLike: {feel_temp}F | Humidity: {humid}% |\n                  UV: {uv} | Wind: {wind_speed}MPH {wind_dir}"
        )

    # KNOWN ERRORS
    elif response.status_code in [404, 500]:

        # LOG WARNING
        logging.warning(
            f"FAILED - Checked city: 'Detroit'. Server responded with status code: {response.status_code}"
        )

    # UNKNOWN ERRORS
    else:
        # LOG WARNING
        logging.warning(
            f"UNKNOWN ERROR - Server responded with status code: {response.status_code}"
        )

# Reveals what unexpected error occurred
except Exception as e:
    print(f"\nThere was an error: {e}\n")

    # LOG ERROR
    logging.error(f"CRASH - Script encountered a critical error: {e}")