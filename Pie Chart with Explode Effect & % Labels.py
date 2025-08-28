
import matplotlib.pyplot as plt

# Data
browsers = ["Chrome", "Firefox", "Edge", "Safari", "Others"]
market_share = [65, 15, 10, 7, 3]

explode = (0.1, 0, 0, 0, 0)  # explode Chrome slice

plt.figure(figsize=(6,6))
plt.pie(market_share, labels=browsers, autopct='%1.1f%%', explode=explode, startangle=140)
plt.title("Pie Chart with % Labels & Explode")
plt.show()
