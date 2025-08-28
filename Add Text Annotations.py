import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, 'r-', label="sin(x)")
plt.title("Experiment 10: Add Text Annotations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

# Add annotation at peak
plt.annotate("Peak", xy=(np.pi/2, 1), xytext=(2, 1.2),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Add annotation at trough
plt.annotate("Trough", xy=(3*np.pi/2, -1), xytext=(5, -1.2),
             arrowprops=dict(facecolor='blue', shrink=0.05))

plt.show()
