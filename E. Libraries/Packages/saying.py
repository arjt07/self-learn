def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")
    
    
def goodbye(name):
    print(f"goodbye, {name}")
    
 
# Execute when the module is not initialized from an import statement 
if __name__ == "__main__":
    main()
     