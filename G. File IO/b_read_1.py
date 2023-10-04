# Read a File
# we don't need to implicitly write "r" when we are Reading...it's Default
'''
with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print("hello,", line.rstrip())
'''

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip()) 
        