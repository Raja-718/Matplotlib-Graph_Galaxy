import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y = np.log(x + 1)

plt.figure(figsize=(10,6), dpi=120)
plt.plot(x, y, 'c-', label="log(x+1)")
plt.title("Experiment 9: Change Figure Size and DPI")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
