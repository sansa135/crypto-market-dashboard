import sqlite3
import pandas as pd

# Connect database
conn = sqlite3.connect("../crypto.db")

# Read processed data
df = pd.read_csv("../data/processed/crypto_clean.csv")

# Load into SQL table
df.to_sql("crypto_market", conn, if_exists="replace", index=False)

conn.close()

print("Data loaded into database successfully!")