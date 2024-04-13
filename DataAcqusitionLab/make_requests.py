import json
import urllib3
from pprintpp import pprint
from my_key import key

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=ST&offset=1&limit=38"
#"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=ST&offset=1"


headers = {
    "token" : key,
    "Content-Type" : "application/json"
}

http =  urllib3.PoolManager()

response = http.request('GET', url, headers=headers)

data = json.loads(response.data.decode('utf-8'))

for i, jobj in enumerate(data['results']):
    #pprint(jobj)
    filename = f"locations_{i}.json"
    with open(filename, 'w') as f:
        json.dump(jobj, f, indent=4)

