import matplotlib.pyplot as plt
import numpy as np

# Data: random test scores for two classes
classA = np.random.normal(70, 10, 100)
classB = np.random.normal(65, 15, 100)

plt.figure(figsize=(6,4))
plt.hist(classA, bins=10, alpha=0.5, label="Class A", color="blue")
plt.hist(classB, bins=10, alpha=0.5, label="Class B", color="red")
plt.title(" Histogram with Two Datasets")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.legend()
plt.show()
