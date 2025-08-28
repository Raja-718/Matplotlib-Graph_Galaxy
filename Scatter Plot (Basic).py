import matplotlib.pyplot as plt
import numpy as np

# Data: random height vs weight
height = np.random.normal(160, 10, 50)
weight = np.random.normal(65, 12, 50)

plt.figure(figsize=(6,4))
plt.scatter(height, weight, color="purple", marker="o")
plt.title("Scatter Plot (Height vs Weight)")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()
