import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**2

plt.figure(figsize=(6,4))
plt.plot(x, y, label="y = x²")
plt.title("Experiment 5: Customize Axis Ranges")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xlim(-5, 5)
plt.ylim(0, 30)
plt.legend()
plt.grid(True)
plt.show()
