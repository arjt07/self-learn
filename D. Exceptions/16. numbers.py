# EXCEPTIONS OR ERROR-HANDLING

# here we can get ValueError if we input float or string
'''
x = int(input("what's x? "))
print(f"x ix {x}") 
'''


# to catch ValueError ot orher types of Errors...use keywords "try" & "except"
'''
try:
    x = int(input("what's x? "))
    print(f"x ix {x}")
except ValueError:
    print("x is not an interger!")
'''

# here we'll get a NameError if we i/p values other than integers
# it's due to the Order of Operation
# values other than int are not being assigned to x, due to the ValueError
'''
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an interger!")  

print(f"x ix {x}")
'''

# to fix the above problem...use "else" keyword
# now it will print x only if the "try" is successful
'''
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an interger!")  
else:
    print(f"x ix {x}")
'''

# in the above it's quitting the program if we enter any wrong value 
# to make it more User Friendly we'll re-prompt the user by using while loop
'''
while True:
    try:
        x = int(input("what's x? "))
        break     
    except ValueError:
        print("x is not an interger!")  
    # else:
    #     break
        
        
print(f"x ix {x}")
'''

# we can make a function of it
def main():
    x = get_int("what's x? ")  # passing prompt as an Argument
    print(f"x ix {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # x = int(input(prompt))
            # return x     
        except ValueError:
            # print("x is not an interger!")
            pass 


main()


# if we want to catch the Error, but not want to prompt anything, 
# we can use the keyword "pass"
# and it's little obnoxious to keep telling the user "x is not an integer" "..."

# we can raise Exceptions by ourself by using keyword "raise"

