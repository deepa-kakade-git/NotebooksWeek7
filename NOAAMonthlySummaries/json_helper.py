import os
import json
import pandas as pd

def read_all_json_files(JSON_ROOT):
    df = pd.DataFrame()
    for filename in os.listdir(JSON_ROOT):
        #if os.path.isfile(JSON_ROOT):  # Check if it's a file
        if '.json' in str(filename):
            with open(os.path.join(JSON_ROOT, filename), 'r') as file:
                json_data = json.load(file)
                df_2 = pd.json_normalize(json_data)
                df_2['source'] = str(filename)
                df = pd.concat([df, df_2])
                print(df)
    return df



