import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Random dataset
df = pd.DataFrame({
    "Math": np.random.randint(60, 100, 20),
    "Science": np.random.randint(55, 95, 20),
    "English": np.random.randint(50, 90, 20),
    "History": np.random.randint(65, 100, 20)
})

corr = df.corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Correlation")
plt.xticks(range(len(corr)), corr.columns, rotation=45)
plt.yticks(range(len(corr)), corr.columns)

# Add text
for i in range(len(corr)):
    for j in range(len(corr)):
        plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", color="black")

plt.title("Correlation Matrix")
plt.show()
