# Dictionary Comprehention 

# using dict comprehention
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors) 


# using list comprehention
'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": "student", "house": "Gyffindor"} for student in students]

print(gryffindors) 
'''

# old school
'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": "student", "house": "Gyffindor"})

print(gryffindors) # list of dictionaries
'''


