import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(6,4))
ax.set_facecolor("#f5f5f5")  # light gray background
ax.plot(x, y, 'r-', linewidth=2)
ax.set_title("Plot with Background Color")
ax.set_xlabel("X")
ax.set_ylabel("sin(x)")
plt.grid(True)
plt.show()
