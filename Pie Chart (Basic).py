
import matplotlib.pyplot as plt

# Data
activities = ["Work", "Study", "Sleep", "Exercise", "Leisure"]
hours = [8, 4, 7, 2, 3]

plt.figure(figsize=(6,6))
plt.pie(hours, labels=activities)
plt.title(" Pie Chart")
plt.show()
