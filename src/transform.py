import pandas as pd

# Read raw crypto data
df = pd.read_csv("../data/raw/crypto_raw.csv")

# Select important columns
columns = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume"
]

df = df[columns]

# Remove null values
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("../data/processed/crypto_clean.csv", index=False)

print("Cleaned crypto data saved successfully!")