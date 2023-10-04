# Properties -> Getter & Setter
class Students:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        
        self._name = name   
    
    # Methods & instance variable inside it, cann't have same NAME
    # GETTER -> in order to ACCESS an Attribute go through some Function
    @property
    def house(self):
        return self._house
    
    # SETTER -> in order to SET an Attribute go through some Function
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        
        self._house = house
        
        
def main():
    student = get_student()  
    print(student)
  
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Students(name, house)
    return student

if __name__ == "__main__":
    main()