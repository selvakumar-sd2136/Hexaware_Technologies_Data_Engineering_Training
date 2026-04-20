import json

with open("students.json", "r") as f:
    data = json.load(f)

students = data["students"]

# 1. Names
print([s["name"] for s in students])

# 2. Python students
print([s["name"] for s in students if s["course"] == "Python"])

# 3. Highest marks
top = max(students, key=lambda x: x["marks"])
print("Topper:", top)

# 4. Average
avg = sum(s["marks"] for s in students) / len(students)
print("Average:", avg)

# 5. Count per course
course_count = {}
for s in students:
    course = s["course"]
    course_count[course] = course_count.get(course, 0) + 1

print(course_count)