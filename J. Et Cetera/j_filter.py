# filter
students = [
    {"name": "Hermione", "house": "Gyffindor"},
    {"name": "Harry", "house": "Gyffindor"},
    {"name": "Ron", "house": "Gyffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])


