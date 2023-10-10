# SUPER class --->
# ---------------

class Wizard:
    def __init__(self, name):
        if not name: 
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
                
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts")
        
print(f"Wizard name is: {wizard.name}") 
print(f"{student.name} is from {student.house}") 
print(f"{professor.name} teaches {professor.subject}") 
  
        