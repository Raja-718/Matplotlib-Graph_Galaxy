import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Simulated stock prices
dates = pd.date_range("2023-01-01", periods=50)
prices = np.random.normal(100, 5, 50).cumsum()

df = pd.DataFrame({"Date": dates, "Price": prices})
df["MA10"] = df["Price"].rolling(10).mean()

plt.figure(figsize=(8,4))
plt.plot(df["Date"], df["Price"], label="Stock Price")
plt.plot(df["Date"], df["MA10"], label="10-Day MA", linewidth=2)
plt.title("Stock Price with Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
