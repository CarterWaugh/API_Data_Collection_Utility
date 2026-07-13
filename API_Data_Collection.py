import requests
import time

print()
city = input("Choose a city to see information on the weather: ").strip().lower()

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    print(f"Server Status Code: {response.status_code}")

    if response.status_code == 200:

        data = response.json()

        current_weather = data['current_condition'][0]

        temp = current_weather['temp_F']
        feel_temp = current_weather['FeelsLikeF']
        humid = current_weather['humidity']
        uv = current_weather['uvIndex']
        wind_dir = current_weather['winddir16Point']
        wind_speed = current_weather['windspeedMiles']

        print()
        print(f"In the city of {city.capitalize()}...")
        print(f"The temperature(F) is : {temp}°, but feels like: {feel_temp}°.")
        print(f"The humidity level is a: {humid}.")
        print(f"The uv index is at a: {uv}.")
        print(f"The direction of the wind on a 16 point is: {wind_dir}, and the speed is {wind_speed} MPH.")
        print()

except Exception as e:
    print(f"An error occurred: {e}")
