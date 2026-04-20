
import csv

with open("data.csv","r") as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)

# Read as Dictionary format

with open("data.csv","r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        print(row["name"],row["marks"])