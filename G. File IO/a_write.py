name = input("What's your name? ")

# open function -> open a file , read info, write info
# w => write, a => append, r => read 

# file = open("names.txt", "w")
# file.write(name)
# file.close()

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# if we want to get rid of .close() function...can use "with" keyword
# "with" automatically opens & closes a file

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
