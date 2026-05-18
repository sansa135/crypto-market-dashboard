import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Read processed data
df = pd.read_csv("../data/processed/crypto_clean.csv")

# Create simple feature
df = df.head(10)

# X and y values
X = np.array(range(len(df))).reshape(-1, 1)

y = df["current_price"]

# Train model
model = LinearRegression()

model.fit(X, y)

# Predict future prices
future_days = np.array(range(len(df) + 5)).reshape(-1, 1)

predictions = model.predict(future_days)

# Plot graph
plt.plot(X, y, label="Actual Prices")

plt.plot(future_days, predictions, label="Predicted Prices")

plt.xlabel("Days")
plt.ylabel("Price")

plt.title("Crypto Price Prediction")

plt.legend()

plt.show()

print("Prediction completed successfully!")