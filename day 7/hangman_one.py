import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    print(display)
    
    if "_" not in display:
        game_over = True
        print("You Win")