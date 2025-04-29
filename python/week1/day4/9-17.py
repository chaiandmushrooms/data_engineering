import pandas as pd
import os

df = pd.read_csv(os.getcwd() + "/raw_data/lfb9-17.csv", dtype={'IncidentNumber': str,
                                                               'NumCalls': str,
                                                               'NumPumpsAttending': str})
df = df[['IncidentNumber',
         'DateOfCall',
         'CalYear',
         'HourOfCall',
         'IncidentGroup',
         'StopCodeDescription',
         'PropertyType',
         'Postcode_full',
         'Latitude',
         'Longitude',
         'NumPumpsAttending',
         'Notional Cost (£)',
         'NumCalls']]

df.drop_duplicates(inplace = True)
df.dropna(inplace = True)
df.to_csv(os.getcwd() + "/clean_data/09-17.csv", index = False)