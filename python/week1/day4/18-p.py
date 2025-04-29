import pandas as pd
import os

df = pd.read_csv(os.getcwd() + "/raw_data/lfb18-p.csv", dtype = {'IncidentNumber': str,
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

df.dropna(inplace = True)
df.drop_duplicates(inplace = True)
df.to_csv(os.getcwd() + "/clean_data/18-present.csv", index = False)