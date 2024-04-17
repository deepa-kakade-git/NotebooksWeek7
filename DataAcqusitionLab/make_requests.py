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

http =  urllib3.PoolManager() #creates an instance of the PoolManager class from the urllib3
# library and assigns it to the variable http.
#urllib3 is a Python library that provides powerful, user-friendly HTTP client functionality.
#TPoolManager is a class within the urllib3 library that manages a pool of connections to a specific host, allowing


response = http.request('GET', url, headers=headers)

data = json.loads(response.data.decode('utf-8'))

for i, jobj in enumerate(data['results']):
    #pprint(jobj)
    filename = f"locations_{i}.json"
    with open(filename, 'w') as f:
        json.dump(jobj, f, indent=4)

# for jobj in data['results']:
#     #pprint(jobj)
#     filename = "location.json"  # Generate a fixed filename
#     with open(filename, 'w') as f:
#         json.dump(jobj, f, indent=4)