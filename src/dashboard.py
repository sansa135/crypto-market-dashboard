import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh

# Page title
st.title("🚀 Crypto Market Dashboard")
# Auto refresh every 30 seconds
st_autorefresh(interval=30000, key="crypto_refresh")

# Read data
df = pd.read_csv("../data/processed/crypto_clean.csv")

# Show dataframe
st.subheader("Crypto Market Data")
st.dataframe(df)

# Top 10 cryptos
top10 = df.head(10)

# Graph
fig, ax = plt.subplots()

ax.bar(top10["name"], top10["current_price"])

ax.set_xlabel("Cryptocurrency")
ax.set_ylabel("Price (USD)")
ax.set_title("Top 10 Cryptocurrency Prices")

st.pyplot(fig)

# Market Cap Section
st.subheader("Market Capitalization")

fig2, ax2 = plt.subplots()

ax2.pie(
    top10["market_cap"],
    labels=top10["name"],
    autopct='%1.1f%%'
)

st.pyplot(fig2)
from sklearn.linear_model import LinearRegression
import numpy as np

st.subheader("📈 AI Price Prediction")

X = np.array(range(len(top10))).reshape(-1, 1)

y = top10["current_price"]

model = LinearRegression()

model.fit(X, y)

future_days = np.array(range(len(top10) + 5)).reshape(-1, 1)

predictions = model.predict(future_days)

fig3, ax3 = plt.subplots()

ax3.plot(X, y, label="Actual Prices")

ax3.plot(future_days, predictions, label="Predicted Prices")

ax3.legend()

st.pyplot(fig3)