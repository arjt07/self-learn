'''
# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from Str
name = name.strip()

# Capitalize user's name
name = name.capitalize()  # capitalize first letter only
name = name.title()       # capitalize first letter of every word
'''
# we can also write as 
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {first}")

