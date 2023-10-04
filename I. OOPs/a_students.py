# classes -> allows us to create our own Datatype & name them
# self -> reference to the current Object

class Student:
    # init method -> initialization Method
    def __init__(self, name, house, patronus):
        # Raising Exceptions
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        
        self.name = name
        self.house = house
        self.patronus = patronus
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌" 
            case "Otter":
                return "🦦" 
            case "Jack Russell Terrier":
                return "🐶" 
            case _:
                return "🪄" 


def main():
    student = get_student()
    print(student)
    print("Expecto Petronum!")
    print(student.charm())
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)  # Constructer
    return student    
    
'''
# using Objects
def get_student():
    student = Student()
    # instance variable -> name & house are variables inside an Object,-
    # -whose Datatype is Student
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
'''

'''
# using Dictionary
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
'''
 
'''
# using List
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # return name, house  # returns a single value, a tuple containing name & house
    return [name, house]
'''


if __name__ == "__main__":
    main()
