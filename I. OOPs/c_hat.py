import random


# without using @classmethod --->
# here sort method is handled by the instance of the class 'Hat'
# --------------------------------------------------------------
# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("Harry")



# using @classmethod
# can run the 'sort' mathod from class, without creating any instance
# --------------------------------------------------------------------
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod    
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")







