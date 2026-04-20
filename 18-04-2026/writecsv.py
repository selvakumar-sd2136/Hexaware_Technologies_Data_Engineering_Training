import csv


data=[
    ["name","marks"],
    ["Priya",88],
    ["Karan",75]
]

with open("writecsv.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)
