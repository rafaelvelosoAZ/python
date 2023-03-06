# #step1

# #Step 1 

word_list = ["aardvark", "baboon", "camel"]

# #TOdo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)

# #TOdo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: \n").lower()

# #Todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  ## print the numbers from 0 through 99

n = chosen_word.count(guess)
if n > 0:
    print(f" We were able to find your guess {n} times, Great!!")
else:
    print("We were not able to find your guess, I'm Sorry!")
print(f"The word chosen was {chosen_word}!")
