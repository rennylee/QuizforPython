import pandas as pd
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&hourly=temperature_2m"

res = requests.get(url)

if res.status_code ==200 :
    data = res.json()
    hourly_data = data.get("hourly", {})
    df = pd.DataFrame(hourly_data)
    print(df.head())