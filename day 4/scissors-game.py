import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#Player1
player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors!\n"))
if player1 == 0:
    print(rock)
elif player1 == 1:
    print(paper)
elif player1 >= 3:
    print("Out of the range!!!!")
elif player1 < 0:
    print("Out of the range!!!")
else:
    print(scissors)

###Computer
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

###Result
if player1 == 0 and computer == 2:
    print("You Won!!")
elif player1 == 1 and computer == 0:
    print("You Won!!")
elif player1 == 2 and computer == 1:
    print("You Won!!")
elif player1 == 2 and computer == 0:
    print("You Lose!!")
elif player1 == 1 and computer == 2:
    print("You Lose!!")
elif player1 == 0 and computer == 1:
    print("You Lose!!")

else:
    print("Drawn!")






