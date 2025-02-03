import pandas as pd
import json

# Read the Excel file
excel_file = '20210309_2020_1 - 4 (1) (1) (1) (1).xls'  # Replace with your actual file path
df = pd.read_excel(excel_file, engine='xlrd')

# Convert the DataFrame to a list of dictionaries (JSON-like format)
json_array = df.to_dict(orient='records')

# Optional: Save the JSON array to a file for later use
with open('output.json', 'w') as json_file:
    json.dump(json_array, json_file, indent=4)
