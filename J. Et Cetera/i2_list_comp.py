# List Comprehensions
students = [
    {"name": "Hermione", "house": "Gyffindor"},
    {"name": "Harry", "house": "Gyffindor"},
    {"name": "Ron", "house": "Gyffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

