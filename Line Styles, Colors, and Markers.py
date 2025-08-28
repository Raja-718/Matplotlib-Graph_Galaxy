
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot
plt.figure(figsize=(6,4))
plt.plot(x, y1, 'r--', label="sin(x) - red dashed")    # red dashed line
plt.plot(x, y2, 'g-o', label="cos(x) - green circles") # green line + circle markers
plt.title("Experiment 3: Line Styles, Colors & Markers")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
