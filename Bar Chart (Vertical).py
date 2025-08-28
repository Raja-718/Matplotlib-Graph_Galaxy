import matplotlib.pyplot as plt

# Data
categories = ["Math", "Science", "English", "History", "Art"]
scores = [85, 90, 78, 88, 76]

plt.figure(figsize=(6,4))
plt.bar(categories, scores, color="skyblue")
plt.title("Experiment 11: Vertical Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()
