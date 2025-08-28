import matplotlib.pyplot as plt
import numpy as np

# Grid data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(6,4))
plt.contour(X, Y, Z, colors="black")
plt.title("Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
