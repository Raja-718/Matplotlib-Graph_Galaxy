import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sqrt(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, 'm-', label="sqrt(x)")
plt.title("Experiment 7: Gridlines Customization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.7)
plt.show()
