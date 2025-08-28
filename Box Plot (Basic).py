import matplotlib.pyplot as plt
import numpy as np

# Random data
data = np.random.normal(50, 10, 200)

plt.figure(figsize=(6,4))
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()
