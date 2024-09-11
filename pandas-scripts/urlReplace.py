import pandas as pd
import json

# Load the CSV file
data = pd.read_csv('/Users/sidv/Downloads/csvHref.csv')

# Load the JSON file
with open('/Users/sidv/Downloads/engblogs.json', 'r') as f:
    json_data = json.load(f)

# Update the JSON data using the CSV data
for index, row in data.iterrows():
    url = row['URL']
    redirect_url = row['Redirect URL']
    for item in json_data:
        if item['url'] == url:
            item['url'] = redirect_url

# Write the updated JSON data back to the file
with open('/Users/sidv/Downloads/engblogs.json', 'w') as f:
  json.dump(json_data, f)