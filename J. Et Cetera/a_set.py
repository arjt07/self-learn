# set in python
students = [
    {"name": "Hermione", "house": "Gyffindor"},
    {"name": "Harry", "house": "Gyffindor"},
    {"name": "Ron", "house": "Gyffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


houses = set()

for student in students:
    # append for list, but add for Set
    houses.add(student["house"])
    
for house in sorted(houses):
    print(house)





'''
houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
'''
