import requests
import config
import csv

LOCATION = 'Bangalore'
KEY = config.WEATHER_API_KEY
API_CALL = 'https://api.waqi.info/feed/{}/?token={}'.format(LOCATION, KEY)

data = requests.request("GET", API_CALL).json()
if data["status"] != 'ok':
    print("Error while requesting the file, exiting program\nResponse code: {}".format(data.status_code))
else:
    values = [data["data"]["time"]["s"],
              LOCATION,
              data["data"]["aqi"],
              data["data"]["idx"],
              data["data"]["dominentpol"],
              data["data"]["iaqi"]["pm10"]["v"],
              data["data"]["iaqi"]["pm25"]["v"]
              ]
    
    with open("air_quality_index.csv", "a") as writer:
        datawrite = csv.writer(writer)
        datawrite.writerow(values)
        print("success \\o/\nsee you tomorrow +_+")

