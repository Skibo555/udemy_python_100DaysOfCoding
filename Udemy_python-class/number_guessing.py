# A welcome message
print("Welcome to the Number Guessing Game!")

# The thought of the computer
print("I'm thinking of a number between 1 and 100 in my head.")

# import random module
import random

number_in_mind = random.randrange(1, 101)

# Choose Difficulty level (Hard and Easy.. Esay has 10 Attempts and Hard has 5 attempts)
def difficulty_level(level_chose):
    if level_chose == "hard":
        level_chose = 5
        return level_chose
    elif level_chose == "easy":
        level_chose = 10
        return level_chose


# Assign level of attempt in accordance to the difficulty lovel chosen by the user.

level = difficulty_level(input("Choose a difficulty level. Type 'hard' or 'easy'. ").lower())


# The user makes a guess

## A while loop to continue looping through the code until the user gets it right before the user exhuasts the trials.
while level > 0:
    user_guess = int(input("Make a guess: "))
        # Compare the guess with the number that's in the mind of the computer
    if number_in_mind > user_guess:
        level -= 1
        print("Too low!")
        print("You have {} attempts left.".format(level))
    elif user_guess > number_in_mind:
        level -= 1
        print("Too high!")
        print("You have {} attempts left.".format(level))
    elif user_guess == number_in_mind:
        print("You got it! The answer was {}.".format(number_in_mind))
        break

    ## if the user_guess is lower than the value that the computer has in mind:
    ## print Too high
    ## print number of attempts that he/she has left.
    ## else:
    ## Print Too low
