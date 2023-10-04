# importing random library
'''
# importing a specific function from Random
from random import choice

coin = choice(["heads", "tails"])
print(coin)
''' 

import random  # importing everything from random

coin = random.choice(["heads", "tails"])
print(coin)

# generate a random no b/w 1 & 10 including 1 & 10
number = random.randint(1, 3)  
print(number)

# random.shuffle(x) -> it takes a LIST of values and shuffles them
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


















