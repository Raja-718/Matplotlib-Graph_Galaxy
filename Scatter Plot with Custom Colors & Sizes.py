
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)   # random colors
sizes = 1000 * np.random.rand(50)  # random bubble sizes

plt.figure(figsize=(6,4))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(label="Color Scale")
plt.title("Scatter Plot with Colors & Sizes")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
