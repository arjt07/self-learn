def main():
    print_column(3)
    print_row(4)
    print_squre(3)
    
    
def print_column(height):
    # for _ in range (height):
    #     print("#")
    print("#\n" * height, end="")   
    
    
def print_row(width):
    print("?" * width)
    
    
def print_squre(size):
    for i in range(size):
        # for j in range(size):
        #     print("#",end="")
        # print()
        
        # print("#" * size)
        
        print_row(size)
        
main()
