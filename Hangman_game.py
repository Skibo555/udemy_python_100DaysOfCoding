#Step 1 
import random

import hangman_words
import hangman_art

# word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(hangman_words.word_list).lower()

print(hangman_art.logo)

print(f'Pssst, the solution is {random_word}.')

# To represent the random word chosen by the random module with "-"
display = []
for letter in random_word:
    display += '-'
print(display)

game_over = False
number_of_life = len(random_word)
while not game_over:
    guessed_char = input("Guess a letter: ")
    if guessed_char in display:
        print("You have already used {} before".format(guessed_char))

    for i in range(0, len(random_word)):
        char = random_word[i]
        if char == guessed_char:
            display[i] = char
    if guessed_char not in random_word:
        print("You guessed {}, and it is not in the secret word. \nYou loos a Life".format(guessed_char))
        print(hangman_art.stages[number_of_life])
        number_of_life -= 1
        if number_of_life == 0:
            game_over = True
            print("You lost!")
    print(display)

    if "-" not in display:
        game_over = True
        print("You win!")