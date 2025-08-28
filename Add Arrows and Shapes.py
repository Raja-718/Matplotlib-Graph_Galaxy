import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, 'b-')
plt.title("Adding Arrows and Shapes")
plt.xlabel("X")
plt.ylabel("sin(x)")

# Arrow
plt.annotate("Peak", xy=(np.pi/2, 1), xytext=(2, 1.2),
             arrowprops=dict(facecolor='red', shrink=0.05))

# Rectangle
plt.gca().add_patch(plt.Rectangle((5, -1), 2, 0.5, fill=False, edgecolor="green", linewidth=2))

plt.grid(True)
plt.show()
