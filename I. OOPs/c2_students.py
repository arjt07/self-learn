class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    # can call this method without instantiating an OBJECT of Student class
    @classmethod  
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)  # automatically passing Reference to itself



def main():
    student = Student.get()
    print(student)
       

if __name__ == "__main__":
    main()
