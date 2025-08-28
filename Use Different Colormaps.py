import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
z = np.random.rand(50)
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(6,4))
plt.scatter(x, y, c=z, cmap='plasma', s=100)
plt.colorbar(label="Values")
plt.title("Scatter with Plasma Colormap")
plt.show()
