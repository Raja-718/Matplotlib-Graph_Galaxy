import matplotlib.pyplot as plt
import numpy as np

# Grid data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

plt.figure(figsize=(6,4))
cp = plt.contourf(X, Y, Z, cmap="coolwarm")
plt.colorbar(cp, label="Value")
plt.title("Filled Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
