# unpacking -> unpacking a single value & putting it into two variables
def total(galleones, sickles, knuts):
    return (galleones * 17 + sickles) * 29 + knuts


# unpacking coins Dictionary with a **
# (**coin) has the same effect as -> (galleones=100, sickles=50, knuts=25)
coins = {"galleones": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "knuts") 


'''
# unpacking coins list with a *
coins = [100, 50, 25]
print(total(*coins), "knuts")  
'''


'''
# can use _, if we are not using the value
first, _ = input("What's your name? ").split(" ")  # unpacking

print(f"hello, {first}")
'''