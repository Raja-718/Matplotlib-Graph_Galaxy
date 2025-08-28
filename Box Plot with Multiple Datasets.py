import matplotlib.pyplot as plt
import numpy as np

# Random datasets
data1 = np.random.normal(50, 10, 200)
data2 = np.random.normal(60, 15, 200)
data3 = np.random.normal(55, 20, 200)

plt.figure(figsize=(6,4))
plt.boxplot([data1, data2, data3], labels=["Group A", "Group B", "Group C"])
plt.title("Multiple Box Plots")
plt.ylabel("Values")
plt.show()
