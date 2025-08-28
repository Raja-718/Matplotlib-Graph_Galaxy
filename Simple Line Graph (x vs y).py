
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = x

# Plot
plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.title("Experiment 1: Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
