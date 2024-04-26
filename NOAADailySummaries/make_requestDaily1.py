import json
import os

import urllib3  #allows you to make various types of HTTP requests
from pprintpp import pprint
from my_key import key

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01 &enddate=2018-01-31 &offset=1#data"


headers = {
    "token" : key,
    "Content-Type" : "application/json"
}

#params = {'datasetid': 'GHCND', 'locationid': 'FIPS:10003', 'startdate' : '2018-01-01', 'enddate' : '2018-01-31', 'offset' : '1'}
http = urllib3.PoolManager()

response = http.request('GET', url, headers=headers)
if response.status == 200:
    data = json.loads(response.data.decode('utf-8'))

    # # Create a folder to store the JSON files
    # folder_name = "json_files"
    # os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist

    for i , jobj1 in enumerate(data):
        filename = f"daily_summaries_FIPS10003_jan_2018_{i}.json"
        with open(filename, 'w') as f:
            json.dump(jobj1, f, indent=4)
else:
    print("Error: Unable to retrieve data. Status code:", response.status)