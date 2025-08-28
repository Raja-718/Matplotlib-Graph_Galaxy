
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2018", "2019", "2020", "2021"]
cityA = [20, 34, 30, 35]
cityB = [25, 32, 34, 20]

x = np.arange(len(years))
width = 0.35

plt.figure(figsize=(6,4))
plt.bar(x - width/2, cityA, width, label="City A")
plt.bar(x + width/2, cityB, width, label="City B")

plt.xticks(x, years)
plt.title("Experiment 14: Grouped Bar Chart")
plt.xlabel("Year")
plt.ylabel("Population (in thousands)")
plt.legend()
plt.show()
