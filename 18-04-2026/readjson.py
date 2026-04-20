import json

with open("exmp.json","r") as file:
    data=json.load(file)
print(data)

for student in data["students"]:
    print(student["name"],student["marks"])
    