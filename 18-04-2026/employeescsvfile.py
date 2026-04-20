import csv

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    employees = list(reader)

# 1. Names
print([e["name"] for e in employees])

# 2. IT employees
print([e["name"] for e in employees if e["department"] == "IT"])

# 3. Average salary
avg = sum(int(e["salary"]) for e in employees) / len(employees)
print("Average salary:", avg)

# 4. Highest salary
top = max(employees, key=lambda x: int(x["salary"]))
print("Highest:", top)

# 5. Department count
dept = {}
for e in employees:
    d = e["department"]
    dept[d] = dept.get(d, 0) + 1

print(dept)