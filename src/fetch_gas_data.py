# src/fetch_gas_data.py
import requests, pandas as pd

API_KEY = "QPAQMY1K9KM3F5T39MXVY32Z2I1C73WSBW"
url = f"https://api.etherscan.io/v2/api?chainid=1&module=gastracker&action=gasoracle&apikey={API_KEY}"


resp = requests.get(url).json()
print(resp)
