from higher_or_lower_art import logo, vs
from higher_or_lower_data import data
import random

print(logo)

def select(data):
    """Selects a random character from the data."""
    return random.choice(data)

def compare_followers(character1, character2):
    """Compares the follower counts of two characters and returns the result."""
    if character1["follower_count"] > character2["follower_count"]:
        return "A"
    else:
        return "B"

score = 0
wants_to_continue = True
previous_b_character = None

while wants_to_continue:
    """This part of the code is responsible for making sure the Previous B become
    A and a new data is being generated to compare against and will be named B"""
    character1 = previous_b_character if previous_b_character else select(data)  # Use previous B if available
    character2 = select(data)

    while character1 == character2:
        character2 = select(data)

    print(f"Compare A: {character1['name']}, a {character1['description']}, from {character1['country']}.")
    print(vs)
    print(f"Against B: {character2['name']}, a {character2['description']}, from {character2['country']}.")

    correct_answer = compare_followers(character1, character2)

    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")
        previous_b_character = character2  # Retain the current B character for the next comparison
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        wants_to_continue = False