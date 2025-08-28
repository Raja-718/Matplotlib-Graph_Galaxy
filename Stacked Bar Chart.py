
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2018", "2019", "2020", "2021"]
men = [20, 35, 30, 35]
women = [25, 32, 34, 20]

x = np.arange(len(years))

plt.figure(figsize=(6,4))
plt.bar(x, men, label="Men", color="blue")
plt.bar(x, women, bottom=men, label="Women", color="pink")

plt.xticks(x, years)
plt.title(" Stacked Bar Chart")
plt.xlabel("Year")
plt.ylabel("Participants")
plt.legend()
plt.show()
