import random

print("Welcome to virtual coin toss program!")
random = random.randint(0, 1)

if random == 0:
    print("Tails")
else:
    print("Heads")