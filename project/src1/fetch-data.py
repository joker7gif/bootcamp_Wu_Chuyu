import os
import yfinance as yf
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

data_dir = os.getenv("DATA_DIR", "data/TSLA")
os.makedirs(data_dir, exist_ok=True)

ticker = yf.Ticker("TSLA")
df = ticker.history(period="3y")

today_str = datetime.today().strftime("%Y%m%d")
filename = f"TSLA_3y_{today_str}.csv"
file_path = os.path.join(data_dir, filename)

df.to_csv(file_path, index=True)
print(f"Data saved to {file_path}")

print("First 5 rows:")
print(df.head())
print("\nData Info:")
print(df.info())
