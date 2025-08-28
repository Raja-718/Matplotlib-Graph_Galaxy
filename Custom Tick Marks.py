import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, 'g-')
plt.title("Custom Tick Marks")
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ["0", "π/2", "π", "3π/2", "2π"])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.grid(True)
plt.show()
