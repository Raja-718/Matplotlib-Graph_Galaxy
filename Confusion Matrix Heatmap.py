import matplotlib.pyplot as plt
import numpy as np

conf_matrix = np.array([[50, 2, 1],
                        [5, 45, 3],
                        [2, 4, 48]])

plt.figure(figsize=(6,5))
plt.imshow(conf_matrix, cmap="Blues")
plt.colorbar(label="Count")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Add text labels
for i in range(3):
    for j in range(3):
        plt.text(j, i, conf_matrix[i, j], ha="center", va="center", color="black")

plt.show()
