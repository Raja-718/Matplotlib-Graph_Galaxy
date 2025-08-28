import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = [2, 4, 6, 8, 10]
errors = [0.2, 0.4, 0.3, 0.5, 0.4]

plt.figure(figsize=(6,4))
plt.errorbar(x, y, yerr=errors, fmt='o-', color="purple", ecolor="black", capsize=5)
plt.title("Plot with Error Bars")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
