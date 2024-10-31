import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

DATABASE_HOST = parser.get(section='database', option='database_host')
DATABASE_NAME = parser.get(section='database', option='database_name')
DATABASE_PORT = parser.get(section='database', option='database_port')
DATABASE_USER = parser.get(section='database', option='database_username')
DATABASE_PASSWORD = parser.get(section='database', option='database_password')

INPUT_PATH = parser.get(section='file_paths', option='input_path')
OUTPUT_PATH = parser.get(section='file_paths', option='output_path')

AWS_ACCESS_KEY = parser.get(section='AWS', option='access_key')
AWS_SECRET_ACCESS_KEY = parser.get(section='AWS', option='secret_access_key')
AWS_BUCKET_NAME = parser.get(section='AWS', option='bucket_name')
AWS_BUCKET_FILENAME = parser.get(section='AWS', option='file_name')


COIN_IDS = [
    'bitcoin', 'ethereum', 'tether', 'binancecoin', 'solana',
    'usd-coin', 'ripple', 'lido-dao', 'dogecoin', 'tron',
    'cardano', 'staked-ether', 'avalanche-2',
    'shiba-inu', 'wrapped-bitcoin', 'weth', 'chainlink',
    'bitcoin-cash', 'polkadot'
]

COLUMNS = [
    'id',
    'name',
    'current_price',
    'market_cap',
    'market_cap_rank',
    'total_volume',
    'high_24h',
    'low_24h',
    'circulating_supply',
    'total_supply',
    'max_supply'
]