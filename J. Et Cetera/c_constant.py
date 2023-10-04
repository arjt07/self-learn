# constant
# CAPITALIZING variable name is a visual indecator that it's a constnant-
# -but python doesn't prevent from changing it
class Cat:
    MEOWS = 3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow!")

cat = Cat()
cat.meow()

'''MEOWS = 3

for _ in range(MEOWS):
    print("meow!")'''