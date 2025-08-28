import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111, projection="3d")

t = np.linspace(0, 20, 100)
x = np.sin(t)
y = np.cos(t)
z = t

ax.plot3D(x, y, z, 'blue')
ax.set_title("3D Line Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
