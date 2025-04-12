import config
import datetime
import json
import requests
import csv

api_key = config.API_KEY
enddate = datetime.date.today()
startdate = enddate - datetime.timedelta(365)

url = 'https://api.oikolab.com/weather'

rows = requests.get(url,
                 params={'param': 'temperature',
                         'location': 'Bengalūru, Karnātaka, India',
                         'start': startdate,
                         'end': enddate},
                 headers={'api-key': api_key}
                 )

if rows.status_code != 200:
     print("Request did not return what was intended.")
     exit()
else:
    weather_data = json.loads(rows.json()['data'])

    with open("hot_weather_data.csv", "w") as datafile:
            fields = ["Date","temperature (degC)"]
            filepointer = csv.DictWriter(datafile, fieldnames = fields)
            filepointer.writeheader()
            length = len(weather_data['index'])
            for i in range(length):
                date = datetime.datetime.fromtimestamp(weather_data['index'][i], datetime.UTC)
                temp = weather_data['data'][i][4]  # Assuming index 4 is temperature - it is right now.
                if temp > 30:
                    row = {"Date": date,
                            "temperature (degC)": temp}
                    filepointer.writerow(row)