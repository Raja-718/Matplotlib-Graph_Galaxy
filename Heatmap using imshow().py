import matplotlib.pyplot as plt
import numpy as np

# Random matrix
data = np.random.rand(6,6)

plt.figure(figsize=(6,4))
plt.imshow(data, cmap="viridis", interpolation="nearest")
plt.colorbar(label="Scale")
plt.title("Heatmap using imshow()")
plt.show()
