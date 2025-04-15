from io import StringIO
import pandas
import requests
import config
import csv

LOCATION = 'Bangalore'
KEY = config.WEATHER_API_KEY
API_CALL = 'https://api.waqi.info/feed/{}/?token={}'.format(LOCATION, KEY)

r = requests.get(API_CALL)

if (r.status_code != 200):
    print("API CALL did not connect as intended ):")
    exit(1)
else:
    pd_instace = pandas.read_json(StringIO(r.text))
    pd_instace.to_json("air_quality_index.json")
    print("success\nsee you tomorrow \\o/")