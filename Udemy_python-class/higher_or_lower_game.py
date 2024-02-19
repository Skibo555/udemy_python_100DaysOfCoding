# Import the modules

from higher_or_lower_art import logo, vs
from higher_or_lower_data import data
import random

# Print the logo at the start of the game
print(logo)

#This function generates random dictionary from the data provided.
def random_number_generateor(data):
    """This function takes one positional argument which most be a list of dictionaries, in this case data."""
    selected_character = random.randint(1, len(data) -1)
    return selected_character


# print(selected_character)
def select(data):
    """This function takes in a list of dictionary as an input and get their respective
    values as to the key described in the function. To modify the function, one needs 
    to change the key based on the requrements needed by the programmer. The function is typically meant for this task."""
    selected_character = random_number_generateor(data)
    for index in range(len(data)):
        # compare_a = data[index]
        for i in data[index]:
            chosen = data[selected_character]

    name = chosen.get('name')
    # print(name)

    follower = chosen.get('follower_count')
    # print(follower)

    description = chosen.get("description")
    # print(description)

    country = chosen.get("country")
    # print(country)
    return name, follower, description, country, selected_character

first = "A"
second = "B"
selected_character_list = []

def another_data_to_compare_after_a_win(selected_character_list, data):
    for index in range(len(data)):
        for i in data[index]:
            choose_to_compare2 = data[selected_character_list -1]
            return choose_to_compare2


name, follower, description, country, selected_character = select(data)
print(f"Compare {first}: {name}, a {description}, from {country}.")

print(vs)
should_continue = True
while should_continue:
    name2, follower2, description2, country2, selected_character = select(data)

    selected_character_list.append(selected_character)

    print(selected_character_list)

    correct = input(f"Compare {second}: {name2}, a {description2}, from {country2}.\nWho has more followers? Type 'A' or 'B': ").lower()
    score = 0
    if correct == "a" and follower > follower2:
        score += 1
        print(f"You are right, {name} has more follower than {name2}. You win, your score is {score}")
        print(logo)
        random_number_generateor(data)
        name, follower, description, country, selected_character = select(data)
        print(vs)
        choose_to_compare2 = another_data_to_compare_after_a_win(selected_character_list, data)
        print(choose_to_compare2)
    elif correct == "a" and follower2 > follower: 
        score = 0
        print(follower2)
        print(f"You are wrong, {name} has more follower than {name2}. You lose, your score is {score}")
        should_continue = False
    if correct == "b" and follower2 > follower:
        score += 1
        print(f"You are right, {name} has more follower than {name2}. You win, your score is {score}")
        random_number_generateor(data)
        name2, follower2, description2, country2, selected_character = select(data)
    elif correct == "b" and follower2 > follower:
        score = 0
        print(follower2)
        print(f"You are wrong, {name} has more follower than {name2}. You lose, your score is {score}")
        should_continue = False