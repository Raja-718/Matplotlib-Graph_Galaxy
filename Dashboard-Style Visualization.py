import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2, figsize=(10,6))

axs[0,0].plot(x, np.sin(x), 'r-'); axs[0,0].set_title("sin(x)")
axs[0,1].bar(["A","B","C","D"], [5,7,3,8], color="orange"); axs[0,1].set_title("Bar Chart")
axs[1,0].scatter(np.random.rand(50), np.random.rand(50), c=np.random.rand(50), cmap="viridis"); axs[1,0].set_title("Scatter Plot")
axs[1,1].hist(np.random.randn(1000), bins=20, color="purple"); axs[1,1].set_title("Histogram")

plt.tight_layout()
plt.suptitle("Dashboard Visualization", fontsize=16, y=1.02)
plt.show()
