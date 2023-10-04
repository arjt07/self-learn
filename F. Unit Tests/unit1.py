# Calculator
def takeInput():
    x = int(input("what's x? "))
    print("x squre is", square(x))
    
  
def square(n):
    return n * n
    # return n**2
    # return pow(n, 2)
 
# Execute when the module is not initialized from an import statement 
if __name__ == "__main__":
    takeInput()