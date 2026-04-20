#task 1
with open("website_visits.txt","r") as file:
    visits=[line.strip() for line in file]

#TASK 2
print("Visitors:",visits)

#task 3
print("Total number of visits:",len(visits))

#task 4
print("Unique visitors:",set(visits))

#task 5
count={}
for visit in visits:
    if visit in count:
        count[visit]+=1
    else:
        count[visit]=1
print(count)


#task 6
most_frequent=max(count, key=count.get)
print(most_frequent)

#task 7
import json
with open("products.json", "r") as file:
    data=json.load(file)
products=data["products"]
# task 8
print("Product names and price:")
for p in products:
    print(p["name"],p["price"])

# task 9
product_dict={}
for p in products:
    product_dict[p["product_id"]]={
        "name":p["name"],
        "price":p["price"]
    }
print(product_dict)

# task 10
max_price=max(product_dict.values(),key=lambda x:x["price"])
print("most expensive product:",max_price)

# task 11
min_price=min(product_dict.values(),key=lambda x:x["price"])
print("least expensive product:",min_price)

#task 12
import csv
with open("orders.csv","r") as file:
    reader=csv.DictReader(file)
    orders=list(reader)

# task 13
for o in orders:
    print(o)

# task 14
product_quantity={}
for o in orders:
    pid=o["product_id"]
    qty=o["quantity"]
    if pid in product_quantity:
        product_quantity[pid]+=qty
    else:
        product_quantity[pid]=qty
print("total quantity sold per product:",product_quantity)

# task 15
customer_orders = {}

for o in orders:
    name = o["customer"]

    if name in customer_orders:
        customer_orders[name] = customer_orders[name] + 1
    else:
        customer_orders[name] = 1

print("Orders per customer:", customer_orders)

# task 16

product_revenue={}
total_revenue=0
for o in orders:
    pid=int(o["product_id"])
    qty=int(o["quantity"])
    price=product_dict[pid]["price"]

    revenue=qty*price
    total_revenue+=revenue
    name = product_dict[pid]["name"]


    if name in product_revenue:
        product_revenue[name]+=revenue
    else:
        product_revenue[name]=revenue

#task 17
print("Total revenue:", total_revenue)

#task 18
print("Revenue per product:", product_revenue)
# task 19
top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

#task 20

customer_spending={}
for o in orders:
    name=o["customer"]
    pid=int(o["product_id"])
    qty=int(o["quantity"])
    price=product_dict[pid]["price"]
    amount=qty*price
    if name in customer_spending:
        customer_spending[name]+=amount
    else:
        customer_spending[name]=amount
print("Customer spending:", customer_spending)

# task 21
max_spending=max(customer_spending, key=customer_spending.get)
print("highest spending customer:",max_spending)

#task 22
big_cust=[]
for c in customer_spending:
    if customer_spending[c] > 50000:
        big_cust.append(c)
print("customers spending more than 50000:",big_cust)


#task 23
def load_visits(filename):
    visits = []
    with open(filename, "r") as file:
        for line in file:
            visits.append(line.strip())
    return visits

#task 24

def load_products(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["products"]

#task 25
def load_orders(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        orders = list(reader)
    return orders

visits = load_visits("website_visits.txt")
products = load_products("products.json")
orders = load_orders("orders.csv")

print(orders)
print(product_dict)
print(set(visits))

product_revenue_list = []

for name, revenue in product_revenue.items():
    product_revenue_list.append((name, revenue))

print(product_revenue_list)
print(type(product_revenue_list[0]))

unique_visitors=set(visits)
with open("sales_report.txt", "w") as file:
    file.write("E-Commerce Sales Report\n")
    file.write(f"Total Website Visits: {len(visits)}\n")
    file.write(f"Unique Visitors: {len(unique_visitors)}\n")
    file.write(f"Total Revenue: {total_revenue}\n")
    file.write(f"Top Customer: {max_spending}\n\n")

    file.write("Product Sales\n")
    for p, rev in product_revenue.items():
        file.write(f"{p} -> {rev}\n")



ordered_customers = set()

for name in customer_orders:
    ordered_customers.add(name)

no_order_visitors = set()

for v in unique_visitors:
    if v not in ordered_customers:
        no_order_visitors.add(v)

print("Visitors who visited but never ordered:")
for v in no_order_visitors:
    print(v)

low_visit_customers = []

for c in customer_orders:
    if c in count:
        visits_num = count[c]
    else:
        visits_num = 0

    if visits_num <= 1:
        low_visit_customers.append(c)

print("\nCustomers who ordered but visited <= 1 time:")
for c in low_visit_customers:
    print(c)