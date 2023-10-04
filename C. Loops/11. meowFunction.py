# MEOW Function
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            return n   # another way to break the Loop

def meow(n):
    for _ in range(n):
        print("meow")
        
main()
