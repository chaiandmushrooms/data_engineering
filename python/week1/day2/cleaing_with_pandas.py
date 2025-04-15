import pandas as pd

raw_json = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": "", "city": "Chicago"},
    {"name": "Charlie", "age": 30, "city": ""},
    {"name": "Alice", "age": 25, "city": "New York"},  # duplicate
    {"name": "  ", "age": None, "city": "Los Angeles"},
    {"name": "Eve", "age": 28, "city": "Houston"},
    {"name": None, "age": "", "city": None}
]

pd_instance = pd.DataFrame(raw_json)
pd_instance.drop_duplicates(inplace = True)
pd_instance.replace(r'^\s*$', None, regex=True)
pd_instance.dropna(inplace = True)