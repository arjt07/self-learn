# Generators -> generates values in python from functions

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


# yield -> generates/returns a Row at a time  
def sheep(n):
    for i in range(n):
        yield "🐑" * i


'''
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i) 

    return flock
'''


    
if __name__ == "__main__":
    main()






