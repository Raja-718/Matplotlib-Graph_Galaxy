import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.exp(x)
y2 = np.log(x+1)

fig, ax1 = plt.subplots(figsize=(6,4))

ax1.plot(x, y1, 'b-', label="exp(x)")
ax1.set_xlabel("X")
ax1.set_ylabel("exp(x)", color="b")

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r--', label="log(x+1)")
ax2.set_ylabel("log(x+1)", color="r")

plt.title("Dual Axis Plot")
plt.show()
