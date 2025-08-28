import matplotlib.pyplot as plt
import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [5, 7, 12, 18, 22, 26, 30, 29, 24, 18, 10, 6]

plt.figure(figsize=(7,4))
plt.plot(months, temperature, marker="o", color="red")
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
