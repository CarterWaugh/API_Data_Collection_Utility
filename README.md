# Welcome to the Weather Info CLI

A simple and lightweight Command Line Interface (CLI) application written in Python that fetches and displays real-time weather information for any city using the `wttr.in` API.

## Features

* **Real-time Data:** Fetches live weather conditions via JSON format.
* **Comprehensive Details:** Displays temperature (Fahrenheit), "Feels Like" temperature, humidity levels, UV index, wind direction (16-point compass), and wind speed (MPH).
* **Error Handling:** Features basic error catching to handle connectivity issues or API glitches gracefully.

---

## Prerequisites

Before running the script, ensure you have Python installed on your machine. You will also need the `requests` library.

You can install the required dependency using pip:

```bash
pip install requests
```
## Example output

```
Choose a city to see information on the weather: Detroit

In the city of Detroit...
The nearest region is : Ontario.
The temperature (F) is: 85°, but feels like: 85°.
The humidity level is: 43%.
The uv index is at a: 6.
The direction of the wind on a 16 point is: WSW, and the speed is 4 MPH.
```
---
## API Reference
This project utilizes the free weather forecast service wttr.in.
It queries the endpoint https://wttr.in/{city}?format=j1 to retrieve the data in a structured JSON format.