import sys
import os
import pandas as pd

from etls.blockchain_etl import extract_data, transform_data, load_data_to_csv
from utils.constants import OUTPUT_PATH, COLUMNS, COIN_IDS

def blockchain_pipeline():
    # extraction
    data = extract_data(COIN_IDS)
    df = transform_data(data, COLUMNS)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/blockchain_data.csv'
    load_data_to_csv(df, file_path)
    
    return df