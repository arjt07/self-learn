# foor Loop
for i in [1, 2, 3]:
    print("meow")

for _ in range(3):     # Pythonic thing-> using _ instead of i (don't care about the name)
    print("meow")

# another way to do it
print("meow\n" * 3, end="")


while True:
    n = int(input("what's n? "))
    # if n < 0:
    #     continue # continue the Loop
    # else:
    #     break
    if n > 0:
        break
    
for _ in range(n):
    print("meow")
