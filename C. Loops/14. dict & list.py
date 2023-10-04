students  = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrir"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for s in students:
    print(s["name"], s["house"], s["patronus"], sep=", ")
