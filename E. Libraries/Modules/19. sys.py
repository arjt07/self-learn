# module for Command-Line-Argument
# sys Module (it stands for system)

# sys.argv -> a variable in sys module - argv (Argument Vector)
# it gives the List of the all of the words user typed-in at their prompt- 
# -before hitting the Enter

# sys.exit -> (print the string and) exit the program prematurely
 

import sys

'''
# separating Error Handling & main code

# check for Errors
if len(sys.argv) < 2:
    sys.exit("too few argument")
elif len(sys.argv) > 2:
    sys.exit("too many argument")

# print name tags (main code)
print("hello, my name is", sys.argv[1])
'''
# if we want to iterate over multiple arguments
# to print the specific arguments we can use ":" to get a slice of the List 
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

