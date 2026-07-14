# Imports
import logging
import requests

# Setup the basic logging configuration
logging.basicConfig(filename="weather.log", level=logging.INFO)

# Asks for users chosen city
print()
city = input("Choose a city to see information on the weather: ").strip().lower()

# Updates URL
url = f"https://wttr.in/{city}?format=j1"

# Starts try block
try:
    response = requests.get(url)

    # SUCCESS: Checks if status code is 200 (OK)
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

        print()
        print(f"In the city of {city.capitalize()}...")
        print(f"The nearest region is : {region_val}.")
        print(f"The temperature (F) is: {temp}°, but feels like: {feel_temp}°.")
        print(f"The humidity level is: {humid}%.")
        print(f"The uv index is at a: {uv}.")
        print(
            f"The direction of the wind on a 16 point is: {wind_dir}, and the speed is {wind_speed} MPH."
        )
        print()

        # LOG SUCCESS: Records all the data you collected into the file
        logging.info(
            f"SUCCESS - City: {city.capitalize()} | Region: {region_val} | Temp: {temp}F | FeelsLike: {feel_temp}F | Humidity: {humid}% |\n                  UV: {uv} | Wind: {wind_speed}MPH {wind_dir}"
        )

    # KNOWN ERRORS: returns what happened if city isnt found
    elif response.status_code in [404, 500]:
        print(f"\nServer Status Code: {response.status_code}")
        print("City not found. Please check your spelling and try again.\n")

        # LOG WARNING: Records that the request failed because of a bad city name or server issue
        logging.warning(
            f"FAILED - Checked city: '{city}'. Server responded with status code: {response.status_code}"
        )

    # UNKNOWN ERRORS: Any other status code
    else:
        print(
            f"\nFailed to retrieve data. Server returned status: {response.status_code}\n"
        )

        # 4. LOG WARNING: Records unexpected server responses
        logging.warning(
            f"UNKNOWN ERROR - Server responded with status code: {response.status_code}"
        )

# Reveals what unexpected error occurred
except Exception as e:
    print(f"\nThere was an error: {e}\n")

    # LOG ERROR: Records a system crash (like your computer losing internet completely)
    logging.error(f"CRASH - Script encountered a critical error: {e}")