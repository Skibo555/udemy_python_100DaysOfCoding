# import random

names = names_string.split(',')

import random

num_items = len(names)

random_choice = random.randint(0, names, -1)

person = names[random_choice]

print(person)