import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [120, 150, 180, 200, 250, 300, 280, 270, 220, 190, 160, 140]

plt.figure(figsize=(7,4))
plt.bar(months, sales, color="teal")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
