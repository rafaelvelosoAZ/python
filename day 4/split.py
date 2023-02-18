import random

names_string = input("give me everybody names \n")
names = names_string.split(", ")
num_items = len(names)

random_choice = random.randint(0, num_items -1)
person = names[random_choice]

print(person + " Is going to pay the meal.")

