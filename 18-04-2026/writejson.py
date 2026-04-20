import json

students={
    "students":[
        {"name":"priya","marks":88},
        {"name":"karan","marks":75}
    ]
}
with open("write.json","w") as file:
    json.dump(students,file)

