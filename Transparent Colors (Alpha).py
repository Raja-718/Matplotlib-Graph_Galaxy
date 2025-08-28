import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(200)
y = np.random.randn(200)

plt.figure(figsize=(6,4))
plt.scatter(x, y, color="blue", alpha=0.3)
plt.title("Scatter Plot with Transparency")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
