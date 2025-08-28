import matplotlib.pyplot as plt
import numpy as np

# Random datasets
data = [np.random.normal(mean, std, 100) for mean, std in zip([50, 60, 70], [10, 15, 20])]

plt.figure(figsize=(6,4))
plt.violinplot(data, showmeans=True)
plt.title("Violin Plot")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()
