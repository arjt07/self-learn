'''
# defining Function
def main():
    name = input("what's your name? ")
    hello(name)
    # print(name)

def hello(to = 'world'): # assignning Default Value
    print("hello,", to)
    
main() 
'''
    
def takeInput():
    x = int(input("what's x? "))
    print("x squre is", square(x))
    
 
def square(n):
    # return n * n
    # return n**2
    return pow(n, 2)
 
takeInput()
    