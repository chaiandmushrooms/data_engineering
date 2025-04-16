import requests
import pandas as pd
import config
import os
from datetime import datetime

# Setup
LOCATION = 'Bangalore'
KEY = config.WEATHER_API_KEY
API_CALL = f'https://api.waqi.info/feed/{LOCATION}/?token={KEY}'
CSV_FILE = "/home/mushroomsandchai/Desktop/data_engineering/python/week1/day3/aqi.csv"

# Make the API request
r = requests.get(API_CALL)

if r.status_code != 200:
    print("Could not retrieve data ):")
    exit(1)
else:
    data = r.json()['data']  # Extract only the 'data' part

    # Prepare data for the DataFrame
    values = {
        "time": data["time"]["s"],
        "location": LOCATION,
        "aqi": data["aqi"],
        "index": data["idx"],
        "dominentpol": data["dominentpol"],
        "pm10": data["iaqi"].get("pm10", {}).get("v"),
        "pm25": data["iaqi"].get("pm25", {}).get("v")
    }

    df = pd.DataFrame([values])

    file_exists = os.path.isfile(CSV_FILE)

    df.to_csv(CSV_FILE, mode = 'a', header = not file_exists, index = False)

    print(f'Data saved to CSV successfully @ {datetime.now()}!')