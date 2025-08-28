import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2, figsize=(8,6))

axs[0,0].plot(x, np.sin(x), 'r-'); axs[0,0].set_title("sin(x)")
axs[0,1].plot(x, np.cos(x), 'g-'); axs[0,1].set_title("cos(x)")
axs[1,0].plot(x, np.tan(x), 'b-'); axs[1,0].set_title("tan(x)")
axs[1,1].plot(x, np.exp(x/3), 'm-'); axs[1,1].set_title("exp(x/3)")

plt.tight_layout()
plt.show()
