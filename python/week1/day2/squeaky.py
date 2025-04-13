# does not clean out emptry columns yet

import pandas

pandas_instance = pandas.read_csv('messy.csv')
pandas_instance.drop_duplicates(inplace = True)
pandas_instance.to_csv("squeaky.csv", index = False)