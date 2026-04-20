import json
import csv



#task 1
with open("students.txt","r") as file:
    students=[line.strip() for line in file]

print("Names:",students)

#task 2
print("Total entries:",len(students))

#task 3
unique_students=set(students)
print("unique students:",unique_students)

#task 4
count={}
for s in students:
    if s in count:
        count[s]+=1
    else:
        count[s]=1
print(count)

#task 5
with open("unique_students.txt","w") as file:
    for s in unique_students:
        file.write(s+"\n")

# task 6

with open("marks.json","r") as file:
    data=json.load(file)
students_data=data["students"]

# task 7
for s in students_data:
    print(s["name"],s["marks"])
# task 8
highest_mark=max(students_data,key=lambda x:x["marks"])
print("Highest_mark",highest_mark["name"])

#task 9
lowest_mark=min(students_data,key=lambda x:x["marks"])
print("Lowest_mark",lowest_mark["name"])

#task 10
average_mark=sum(s["marks"] for s in students_data)/len(students_data)
print("Average_mark",average_mark)

#task 11
for s in students_data:
    if s["course"]=="Python":
        print(s["name"])
#task 12
course_count={}
for s in students_data:
    if s["course"] in course_count:
        course_count[s["course"]]+=1
    else:
        course_count[s["course"]]=1
print(course_count)

#task 13
attendance={}
with open("attendance.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        attendance[row["name"]] = {
            "present": int(row["days_present"]),
            "total": int(row["total_days"])
        }

#task 14
for name, data in attendance.items():
    print(name, data)

# Task 15
attendance_percent={}
for name,data in attendance.items():
    percent=(data["present"]/data["total"])*100
    attendance_percent[name] = percent
print(attendance_percent)

#task 16
for name,percent in attendance_percent.items():
    if percent <80:
        print(name, percent)
# task 17
best_attendance=max(attendance_percent,key=attendance_percent.get)
print("Best Attendance:",best_attendance)

#task 18
marks_list = [s["marks"] for s in students_data]

print("\nMarks Analysis:")
print("Highest:", max(marks_list))
print("Lowest:", min(marks_list))
print("Sum:", sum(marks_list))

# task 19
course_tuple=[s["course"] for s in students_data]
print("Courses:",course_tuple)

# task 20
unique_courses=set(course_tuple)
print("Unique Courses:",unique_courses)

#task 21
mark_dict={s["name"]:s["marks"] for s in students_data}
print("Marks:",mark_dict)

#task 22
attendance_dict=attendance_percent
print("Attendance:",attendance_dict)

#task 23
for name,mark in mark_dict.items():
    if mark>=50:
        print(name,"pass")
    else:
        print(name,"fail")
# task 24

for name,mark in mark_dict.items():
    if mark>=90:
        print(name,"GRADE A")
    elif mark>=75:
        print(name,"GRADE B")
    elif mark>=50:
        print(name,"GRADE C")
    else:
        print(name,"fail")

# task 25
print("High Performers:")
for name in mark_dict:
    if name in attendance_dict:
        if mark_dict[name] > 80 and attendance_dict[name] > 85:
            print(name)

# task 26
def read_students():
    with open("students.txt") as f:
        return [line.strip() for line in f]
student_names = read_students()
print("Students:", student_names)

# task 27
def load_marks():
    with open("marks.json") as f:
        return json.load(f)["students"]
students_data = load_marks()
print("Marks Data:", students_data)

# task 28
def load_attendance():
    data = {}
    with open("attendance.csv") as f:
        reader = csv.DictReader(f)
        for r in reader:
            data[r["name"]] = (int(r["days_present"]), int(r["total_days"]))
    return data
attendance_data = load_attendance()
print("Attendance Data:", attendance_data)
#task 29
def avg_marks(students):
    return sum(s["marks"] for s in students) / len(students)
average_marks=avg_marks(students_data)
print("Average Marks:", average_marks)

#task 30
print("Attendance Percentage:")
def calc_attendance_percent(p, t):
    return (p/t)*100
for name, (p, t) in attendance_data.items():
    percent = calc_attendance_percent(p, t)
    print(name, percent)

#task 31
def topper(students):
    return max(students, key=lambda x: x["marks"])
top = topper(students_data)
print("Topper:", top["name"])

#task 32
def grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 50:
        return "C"
    else:
        return "Fail"
print("Grades:")
for s in students_data:
    print(s["name"], grade(s["marks"]))

# task 33 & 34

final_data = {}

for s in students_data:
    name = s["name"]
    final_data[name] = {
        "marks": s["marks"],
        "attendance": attendance_dict[name],
        "course": s["course"],
        "grade": grade(s["marks"])}
print("Final Data:", final_data)
# task 35
eligible_students = []

for name, data in final_data.items():
    if data["marks"] >= 75 and data["attendance"] >= 80:
        eligible_students.append(name)

print("Eligible Students:", eligible_students)

#task 36
need_improvement = []

for name, data in final_data.items():
    if data["marks"] < 75 or data["attendance"] < 80:
        need_improvement.append(name)

print("Students Needing Improvement:", need_improvement)

# task 37
with open("report.txt", "w") as file:
    file.write("Student Report\n")
    for name, data in final_data.items():
        line = f"{name} - Marks: {data['marks']} - Attendance: {data['attendance']:.1f}% - Grade: {data['grade']}\n"
        file.write(line)
# task 38
with open("eligible_students.txt", "w") as file:
    for name in eligible_students:
        file.write(name + "\n")

# task 39
print("\nFinal Output:")
print("Topper:", top["name"])
print("Best Attendance:", best_attendance)
print("Average Marks:", round(average_marks, 1))
print("Eligible Students:", ", ".join(eligible_students))
print("Students Needing Improvement:", ", ".join(need_improvement))
