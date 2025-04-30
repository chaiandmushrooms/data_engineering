import pandas as pd
import sqlite3 as sql
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

conn = sql.connect(os.getcwd() + '/clean_data/fires.db')
df.to_sql('18+', conn, index = False, if_exists = 'replace')