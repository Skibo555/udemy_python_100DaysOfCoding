from higher_or_lower_art import logo, vs
from higher_or_lower_data import data
import random

print(logo)

def random_number_generator(data):
    """This function generates a random index from the data."""
    return random.randint(0, len(data) - 1)

def select(data, index):
    """This function selects a character from the data using the given index."""
    chosen = data[index]
    name = chosen.get('name')
    follower = chosen.get('follower_count')
    description = chosen.get("description")
    country = chosen.get("country")
    return name, follower, description, country

first = "A"
second = "B"
selected_character_list = []

def another_data_to_compare_after_a_win(selected_character_list, data):
    """This function selects another character from the data after a win."""
    index = selected_character_list[-1]  # Get the last index from the list
    return select(data, index)

name, follower, description, country = select(data, random_number_generator(data))
print(f"Compare {first}: {name}, a {description}, from {country}.")

print(vs)

should_continue = True
score = 0

while should_continue:
    name2, follower2, description2, country2 = select(data, random_number_generator(data))
    selected_character_list.append(random_number_generator(data))

    print(selected_character_list)

    correct = input(f"Compare {second}: {name2}, a {description2}, from {country2}.\nWho has more followers? Type 'A' or 'B': ").lower()

    if correct == "a" and follower > follower2:
        score += 1
        print(f"You are right, {name} has more followers than {name2}. You win, your score is {score}")
        name, follower, description, country = select(data, random_number_generator(data))
        print(vs)
    elif correct == "a" and follower2 > follower: 
        score = 0
        print(f"You are wrong, {name} has fewer followers than {name2}. You lose, your score is {score}")
        should_continue = False
    elif correct == "b" and follower2 > follower:
        score += 1
        print(f"You are right, {name} has fewer followers than {name2}. You win, your score is {score}")
        name, follower, description, country = select(data, random_number_generator(data))
        print(vs)
    elif correct == "b" and follower > follower2:
        score = 0
        print(f"You are wrong, {name} has more followers than {name2}. You lose, your score is {score}")
        should_continue = False
