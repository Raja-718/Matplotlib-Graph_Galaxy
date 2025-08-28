import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6,4))
plt.plot(x, y, 'bo-')
plt.title("Customized Fonts", fontsize=18, fontfamily='serif')
plt.xlabel("X values", fontsize=14, fontfamily='monospace')
plt.ylabel("Y values", fontsize=14, fontfamily='monospace')
plt.grid(True)
plt.show()
