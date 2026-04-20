# E-Commerce Capstone Project
# Task 1
with open("website_visits.txt","r") as file:
    visits=[line.strip() for line in file]

# Task 2
print("Visitors:",visits)

# Task 3
print("Total number of visits:",len(visits))

# Task 4
unique_visitors=set(visits)
print("Unique visitors:",unique_visitors)

# Task 5
count={}
for visit in visits:
    count[visit] = count.get(visit, 0) + 1
print(count)

# Task 6
most_frequent=max(count, key=count.get)
print(most_frequent)


# Task 7
import json
with open("products.json", "r") as file:
    data=json.load(file)
products=data["products"]

# Task 8
print("Product names and price:")
for p in products:
    print(p["name"],p["price"])

# Task 9
product_dict={}
for p in products:
    product_dict[p["product_id"]] = {
        "name": p["name"],
        "price": p["price"]
    }

# Task 10
max_price=max(product_dict.values(),key=lambda x:x["price"])
print("most expensive product:",max_price)

# Task 11
min_price=min(product_dict.values(),key=lambda x:x["price"])
print("least expensive product:",min_price)


# Task 12
import csv
with open("orders.csv","r") as file:
    reader=csv.DictReader(file)
    orders=list(reader)

# Task 13
for o in orders:
    print(o)

# Task 14
product_quantity={}
for o in orders:
    pid=int(o["product_id"])
    qty=int(o["quantity"])
    product_quantity[pid] = product_quantity.get(pid, 0) + qty

print("total quantity sold per product:",product_quantity)

# Task 15
customer_orders={}
for o in orders:
    name=o["customer"]
    customer_orders[name] = customer_orders.get(name, 0) + 1

print("Orders per customer:", customer_orders)


# Task 16–18
product_revenue={}
total_revenue=0

for o in orders:
    pid=int(o["product_id"])
    qty=int(o["quantity"])
    price=product_dict[pid]["price"]

    revenue=qty*price
    total_revenue+=revenue

    name=product_dict[pid]["name"]
    product_revenue[name] = product_revenue.get(name, 0) + revenue

# Task 17
print("Total revenue:", total_revenue)

# Task 18
print("Revenue per product:", product_revenue)

# Task 19
top_product=max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)


# Task 20
customer_spending={}
for o in orders:
    name=o["customer"]
    pid=int(o["product_id"])
    qty=int(o["quantity"])
    price=product_dict[pid]["price"]

    amount=qty*price
    customer_spending[name] = customer_spending.get(name, 0) + amount

print("Customer spending:", customer_spending)

# Task 21
max_spending=max(customer_spending, key=customer_spending.get)
print("Highest spending customer:", max_spending)

# Task 22
big_cust=[c for c in customer_spending if customer_spending[c] > 50000]
print("Customers spending more than 50000:", big_cust)


# Task 23
def load_visits(filename):
    with open(filename,"r") as file:
        return [line.strip() for line in file]

# Task 24
def load_products(filename):
    with open(filename,"r") as file:
        data=json.load(file)
    return data["products"]

# Task 25
def load_orders(filename):
    with open(filename,"r") as file:
        return list(csv.DictReader(file))


# Task 26
def calculate_product_revenue(orders, product_dict):
    revenue={}
    for o in orders:
        pid=int(o["product_id"])
        qty=int(o["quantity"])
        name=product_dict[pid]["name"]
        amount=qty*product_dict[pid]["price"]

        revenue[name] = revenue.get(name, 0) + amount
    return revenue


# Task 27
def calculate_customer_spending(orders, product_dict):
    spending={}
    for o in orders:
        name=o["customer"]
        pid=int(o["product_id"])
        qty=int(o["quantity"])
        amount=qty*product_dict[pid]["price"]

        spending[name] = spending.get(name, 0) + amount
    return spending


# Task 28
def find_top_customer(spending):
    return max(spending, key=spending.get)


# Reload using functions
visits = load_visits("website_visits.txt")
products = load_products("products.json")
orders = load_orders("orders.csv")


product_dict={}
for p in products:
    product_dict[p["product_id"]] = {
        "name": p["name"],
        "price": p["price"]
    }


product_revenue = calculate_product_revenue(orders, product_dict)
customer_spending = calculate_customer_spending(orders, product_dict)
top_customer = find_top_customer(customer_spending)

print("Top customer (function):", top_customer)


# Tuple (Data structure requirement)
product_revenue_list=[(name, revenue) for name, revenue in product_revenue.items()]
print(product_revenue_list)


# Final Report
unique_visitors=set(visits)

with open("sales_report.txt","w") as file:
    file.write("E-Commerce Sales Report\n")
    file.write(f"Total Website Visits: {len(visits)}\n")
    file.write(f"Unique Visitors: {len(unique_visitors)}\n")
    file.write(f"Total Revenue: {total_revenue}\n")
    file.write(f"Top Customer: {top_customer}\n\n")

    file.write("Product Sales\n")
    for p, rev in product_revenue.items():
        file.write(f"{p} -> {rev}\n")


# Task 29
ordered_customers=set(customer_orders.keys())
no_order_visitors=unique_visitors - ordered_customers

print("Visitors who visited but never ordered:")
for v in no_order_visitors:
    print(v)


# Task 30
low_visit_customers=[c for c in customer_orders if count.get(c,0) <= 1]

print("\nCustomers who ordered but visited <=1 time:")
for c in low_visit_customers:
    print(c)
