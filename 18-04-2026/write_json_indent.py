import json

students = {
    "students": [
        {"name": "priya", "marks": 88},
        {"name": "karan", "marks": 75}
    ]
}
with open("write_json_with_indent.json", "w") as file:
    json.dump(students, file,indent=4)

