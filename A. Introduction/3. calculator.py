'''
# Addition
# inputs as a String, hence '+' concatinates instead of addition
x = input("what's X? ") 
y = input("what's Y? ")

# converting strings into int/float datatype
# z = int(x) + int(y) 
z = float(x) + float(y) 
z = round(z)  # rounding a Number

# formatting the output
# print(z)
print(f"{z:,}") # o/p no. will be Separated by Comma
'''

# Division
a = float (input("what's a? ")) 
b = float (input("what's b? "))

d = (a * 100) / b

#rounding the o/p no upto 2 digits
# d = round(d)
# print(d)

# another way of Rounding-> Formatting it
print(f"{d:.2f}") # rounding it upto 2 digits using f-string 
