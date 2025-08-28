import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 50)
y = np.exp(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, 'b-', label="exp(x)")
plt.title("Experiment 8: Save Plot as File")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

# Save in multiple formats
plt.savefig("experiment8_plot.png", dpi=300)
plt.savefig("experiment8_plot.jpg", dpi=300)
plt.savefig("experiment8_plot.pdf")

plt.show()
