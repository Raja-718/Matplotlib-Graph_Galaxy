import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(6,4))
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.title("Experiment 6: Sine & Cosine Curve")
plt.xlabel("Angle (radians)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
