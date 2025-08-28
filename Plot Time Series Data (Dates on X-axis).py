import matplotlib.pyplot as plt
import pandas as pd

# Data
dates = pd.date_range("2023-01-01", periods=10)
sales = [200, 220, 250, 240, 260, 300, 280, 310, 330, 350]

plt.figure(figsize=(7,4))
plt.plot(dates, sales, marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
