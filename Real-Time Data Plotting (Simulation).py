import matplotlib.pyplot as plt
import numpy as np
import time

x, y = [], []

plt.ion()
fig, ax = plt.subplots()

for i in range(20):
    x.append(i)
    y.append(np.random.randint(0, 10))
    ax.clear()
    ax.plot(x, y, marker="o")
    ax.set_title("Real-Time Data Plot")
    ax.set_xlabel("Time step")
    ax.set_ylabel("Random Value")
    plt.pause(0.3)

plt.ioff()
plt.show()
