# 
import csv

students = []

# reader function Reads a csv file
with open("students_2.csv") as file:
    # reader = csv.reader(file)   # returns a List
    reader = csv.DictReader(file)   # returns a Dict
    for row in reader:
        # students.append({"name": row[0], "home": row[1]})
        students.append({"name": row["name"], "home": row["home"]})
 
for s in sorted(students, key=lambda x: x["name"]):
    print(f"{s['name']} is from {s['home']}")
            
