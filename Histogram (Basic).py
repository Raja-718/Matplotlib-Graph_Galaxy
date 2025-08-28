import matplotlib.pyplot as plt
import numpy as np

# Data: random ages
ages = np.random.randint(18, 60, 100)

plt.figure(figsize=(6,4))
plt.hist(ages, bins=8, color="green", edgecolor="black")
plt.title(" Histogram of Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
