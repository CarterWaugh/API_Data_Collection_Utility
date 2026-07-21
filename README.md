# Weather Info CLI & API Data Collector
A lightweight, modular Python application that fetches, displays, and logs real-time weather information for Detroit using the ```wttr.in``` API.

This project uses a modular design—separating core API fetching and formatting logic into an importable module (`API_Data_Collection.py`) while keeping execution, custom request headers, and logging configuration in `daily_detroit_weather.py`.

## ✨ Features
* Modular Architecture: Core API functions are isolated in API_Data_Collection.py so they can be easily imported into other scripts.

* Custom Request Headers & Timeout: Includes custom browser-like User-Agent headers and an 8-second timeout limit for network safety.

* Comprehensive Weather Data: Fetches and displays temperature (°F), "Feels Like" temperature, humidity levels, UV index, wind speed (MPH), 16-point wind direction, and nearest region.

* Automated Background Logging: Configures a dedicated logger that records success states, API errors (e.g., 404/500 status codes), and unexpected crashes directly into daily_detroit.log.

* Error Handling: Built-in try/except blocks gracefully catch network glitches and server failures.

## ⚡ Prerequisites
Ensure Python is installed on your machine along with the requests HTTP library:

```bash
pip install requests
```
## 🚀 How to Run
Execute the primary script directly from VS Code or your terminal:
```bash
python daily_detroit_weather.py
```
## 📊 Example Usage & Output
Terminal Display
```plaintext
In the city of Detroit...
The nearest region is : Ontario.
The temperature (F) is: 85°, but feels like: 85°.
The humidity level is: 43%.
The uv index is at a: 6.
The direction of the wind on a 16 point is: WSW, and the speed is 4 MPH.
```
## Generated Background Log (`daily_detroit.log`)
```plaintext
2026-07-21 11:51:55,000 - INFO - SUCCESS - City: Detroit | Region: Ontario | Temp: 85F | FeelsLike: 85F | Humidity: 43% |
                  UV: 6 | Wind: 4MPH WSW
```
## 🌐 API Reference
This project queries the free weather service `wttr.in` via the JSON endpoint:

```plaintext
https://wttr.in/{city}?format=j1
```