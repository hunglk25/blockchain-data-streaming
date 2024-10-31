import requests
import sys
import pandas as pd
from datetime import datetime
import numpy as np
import os

def extract_data(COIN_IDS):
    try:
        ids = ','.join(COIN_IDS)
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={ids}'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(e)
        sys.exit(1)


def transform_data(data, COLUMNS):
    df = pd.DataFrame(data=data)
    df = df[COLUMNS]
    df['time_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df


def load_data_to_csv(data: pd.DataFrame, path: str):
    if os.path.exists(path):
        data.to_csv(path, mode='a', header=False, index=False)
    else:
        data.to_csv(path, mode='w', index=False)