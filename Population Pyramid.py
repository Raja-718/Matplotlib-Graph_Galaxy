import matplotlib.pyplot as plt
import numpy as np

# Age groups
age_groups = ["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71+"]
male = np.array([5, 10, 20, 25, 15, 10, 5, 2]) * -1
female = [4, 12, 22, 20, 18, 12, 6, 3]

plt.figure(figsize=(7,6))
plt.barh(age_groups, male, color="blue", label="Male")
plt.barh(age_groups, female, color="pink", label="Female")
plt.title("Population Pyramid")
plt.xlabel("Population (in thousands)")
plt.ylabel("Age Group")
plt.legend()
plt.show()
