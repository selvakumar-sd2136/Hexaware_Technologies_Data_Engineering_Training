import json

with open("orders.json", "r") as f:
    data = json.load(f)

orders = data["orders"]

# 1. Print all
print(orders)

# 2. Total revenue
total = sum(o["amount"] for o in orders)
print("Total revenue:", total)

# 3. Spending per customer
spending = {}
for o in orders:
    c = o["customer"]
    spending[c] = spending.get(c, 0) + o["amount"]

print("Spending:", spending)

# 4. Highest spender
top = max(spending, key=spending.get)
print("Top customer:", top)

# 5. Order count
count = {}
for o in orders:
    c = o["customer"]
    count[c] = count.get(c, 0) + 1

print("Order count:", count)