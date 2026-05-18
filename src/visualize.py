import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data
df = pd.read_csv("../data/processed/crypto_clean.csv")

# Top 5 cryptos
top5 = df.head(5)

# Create graph
plt.bar(top5["name"], top5["current_price"])

plt.xlabel("Cryptocurrency")
plt.ylabel("Price (USD)")
plt.title("Top 5 Cryptocurrency Prices")

plt.show()
