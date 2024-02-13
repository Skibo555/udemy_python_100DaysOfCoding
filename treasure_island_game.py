print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasue Island. \nYour mission is to find the treasure.")

decision_1 = input("Do you want to go to left or right? ")
coverted_decision_1 = decision_1.lower()

if coverted_decision_1 == 'left':
    print('God save you sha.')
    inner_decision_1 = input("You've arrived at a river, do you want to wait for the arrival of a boat or you want to swim? ")
    converted_inner_inner_decision_1 = inner_decision_1.lower()
    if converted_inner_inner_decision_1 == 'wait':
        inner_decision_2 = input("You have arrived at an entrance that has three doors, they are coloured red, blue and yellow, which one would you choose? ")
        converted_inner_inner_decision_2 = inner_decision_2.lower()
        if converted_inner_inner_decision_2 == 'yellow':
            print("You win, but no too happy, I never good for programming. If I good finish you no go fit win any of my games.")
        else:
            print("Game Over! But you try sha, you made some very good decisions before e spoil for you.")
    else:
        print("Game Over!")
else:
    print("Game Over!")