import matplotlib.pyplot as plt

# Data
companies = ["Google", "Amazon", "Facebook", "Apple", "Microsoft"]
revenue = [182, 386, 86, 274, 143]  # in billions

plt.figure(figsize=(6,4))
plt.barh(companies, revenue, color="orange")
plt.title(" Horizontal Bar Chart")
plt.xlabel("Revenue (Billion USD)")
plt.show()
