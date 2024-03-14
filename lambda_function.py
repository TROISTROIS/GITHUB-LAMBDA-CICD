import json
import requests
import pandas as pd

def lambda_handler(event,context):

    print("Event Data ---->", event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    hard_coded_data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=hard_coded_data)

    print(df)
    print("Done!!!!")
