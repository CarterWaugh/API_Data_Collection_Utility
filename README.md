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
Choose a city to see information on the weather: Chicago

Server Status Code: 200

In the city of Chicago...
The temperature(F) is : 68°, but feels like: 68°.
The humidity level is a: 62.
The uv index is at a: 4.
The direction of the wind on a 16 point is: ENE, and the speed is 7 MPH.
```
---
## API Reference
This project utilizes the free weather forecast service wttr.in.
It queries the endpoint https://wttr.in/{city}?format=j1 to retrieve the data in a structured JSON format.