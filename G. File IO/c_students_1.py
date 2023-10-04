# Reading & Splitting
'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} -> {row[1]}")
'''
# another way to do this
# also Sorting (by Sentences)
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")  # assinging splitted items into two variables
        students.append(f"{name} -> {house}")
        
for s in sorted(students):
    print(s)
'''
    
    
# Sorting (by names or house)
students = []

with open("students_1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")  # assinging splitted items into two variables
        student = {"name": name, "house": house}
        students.append(student)
 
for s in sorted(students, key=lambda student: student["house"]):
    print(f"{s['name']} is in {s['house']}")
            
            