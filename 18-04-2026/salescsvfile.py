import csv

with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    sales = list(reader)

# 1. Total revenue
total = sum(int(s["quantity"]) * int(s["price"]) for s in sales)
print("Total revenue:", total)

# 2 & 4. Quantity + revenue per product
qty = {}
revenue = {}

for s in sales:
    p = s["product"]
    q = int(s["quantity"])
    price = int(s["price"])

    qty[p] = qty.get(p, 0) + q
    revenue[p] = revenue.get(p, 0) + q * price

print("Quantity:", qty)
print("Revenue:", revenue)

# 3. Highest sales product
top = max(revenue, key=revenue.get)
print("Top product:", top)

# 5. Revenue > 50000
for p in revenue:
    if revenue[p] > 50000:
        print(p, revenue[p])