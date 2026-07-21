# Imports
import logging
import requests

# Setup the basic logging configuration
logging.basicConfig(filename="weather.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL and User agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
timeout_seconds = 8

def get_weather_info(city_name):
        
    url = f"https://wttr.in/{city_name}?format=j1"

    # Starts try block to check for errors
    try:
        response = requests.get(url, headers=headers, timeout=timeout_seconds)

        # SUCCESS: Checks if status code is 200, and returns response.JSON()
        if response.status_code == 200:
            return response.json()
            
        # KNOWN ERRORS
        elif response.status_code in [404, 500]:
            print(f"\nServer Status Code: {response.status_code}")
            print("City not found. Please check your spelling and try again.\n")

            # LOG WARNING
            logging.warning(
                f"FAILED - Checked city: '{city_name}'. Server responded with status code: {response.status_code}"
            )

            return None

        # UNKNOWN ERRORS
        else:
            print(
                f"\nFailed to retrieve data. Server returned status: {response.status_code}\n"
            )

            # LOG WARNING
            logging.warning(
                f"UNKNOWN ERROR - Server responded with status code: {response.status_code}"
            )

            return None

    # Reveals what unexpected error occurred
    except Exception as e:
        print(f"\nThere was an error: {e}\n")

        # LOG ERROR
        logging.error(f"CRASH - Script encountered a critical error: {e}")

        return None

def print_weather_report(city_name, data):

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
    print(f"In the city of {city_name.capitalize()}...")
    print(f"The nearest region is : {region_val}.")
    print(f"The temperature (F) is: {temp}°, but feels like: {feel_temp}°.")
    print(f"The humidity level is: {humid}%.")
    print(f"The uv index is at a: {uv}.")
    print(
         f"The direction of the wind on a 16 point is: {wind_dir}, and the speed is {wind_speed} MPH."
    )
    print()

    # LOG SUCCESS
    logging.info(
        f"SUCCESS - City: {city_name.capitalize()} | Region: {region_val} | Temp: {temp}F | FeelsLike: {feel_temp}F | Humidity: {humid}% |\n                  UV: {uv} | Wind: {wind_speed}MPH {wind_dir}"
    )

# Main program
def main():

# Asks for users chosen city
    print()
    city = input("Choose a city to see information on the weather: ").strip().lower()

    # Make sure user didn't just press Enter
    if not city:
        print("You must enter a city name.")
        return

    # Fetch and display
    weather_data = get_weather_info(city)
    if weather_data:
        print_weather_report(city, weather_data)

if __name__ == "__main__":
    main()
