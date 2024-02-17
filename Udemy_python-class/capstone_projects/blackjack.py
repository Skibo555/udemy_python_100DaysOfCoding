from blackjack_art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = random.choices(cards, k=2)
dealer_card = random.choices(cards, k=2)

for card in player_card:
    players_current_card = player_card[0] + player_card[1]

for deck in dealer_card:
    dealers_current_card = dealer_card[0] + dealer_card[1]
print("Your cards are {} current score: {}".format(player_card, players_current_card))
print("Computer's first card: {}".format(dealer_card[0]))

more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
if more_cards == 'y':
    add_more_cards = random.choice(cards)
    player_card.append(add_more_cards)
    added = players_current_card + add_more_cards
    print("Your cards: {}, current score: {}".format(player_card, added))
    print("Computer's first card: {}".format(dealer_card[0]))
    print("Computer's final hand: {}, final score: {}".format(dealer_card[0], dealers_current_card))
    if (players_current_card <= 21) and (dealers_current_card < players_current_card):
        print("You went over. You lose")
    elif dealers_current_card > added and added <= 21:
        print("You won!")
    elif added > 21 and dealers_current_card < 21:
        print("You lose, the computer won!")
    elif added < 21 and dealers_current_card > 21:
        print("You won, the computer loss!")
    elif added == dealers_current_card:
        print("It's a draw!")

elif more_cards == "n":
    if (players_current_card <= 21) and (dealers_current_card < players_current_card):
        print("Computer has the highest score {}".format(dealer_card))
        print("You went over. You lose")
    elif dealers_current_card > players_current_card and players_current_card <= 21:
        print("You won!")
    elif players_current_card > 21 and dealers_current_card < 21:
        print("You lose, the computer won!")
    elif players_current_card < 21 and dealers_current_card > 21:
        print("You won, the computer loss!")
    elif players_current_card == dealers_current_card:
        print("It's a draw!")
        exit()

wants_to_continue = True

while wants_to_continue:

    player_card *= 0
    dealer_card *= 0
    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
    player_card = random.choices(cards, k=2)
    dealer_card = random.choices(cards, k=2)
    for card in player_card:
        players_current_card = player_card[0] + player_card[1]

    for deck in dealer_card:
        dealers_current_card = dealer_card[0] + dealer_card[1]
    print("Your cards are {} current score: {}".format(player_card, players_current_card))
    print("Computer's first card: {}".format(dealer_card[0]))
    if players_current_card <= 21 and dealers_current_card < players_current_card:
        print("You went over. You lose")
    elif dealers_current_card > players_current_card and players_current_card <= 21:
        print("You won!")
    elif players_current_card > 21 and dealers_current_card < 21:
        print("You lose, the computer won!")
    elif players_current_card < 21 and dealers_current_card > 21:
        print("You won, the computer loss!")
    elif players_current_card == dealers_current_card:
        print("It's a draw!")

    more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if more_cards == 'y':
        add_more_cards = random.choice(cards)
        player_card.append(add_more_cards)
        added = players_current_card + add_more_cards
        print("Your cards: {}, current score: {}".format(player_card, added))
        print("Computer's first card: {}".format(dealer_card[0]))
        print("Computer's final hand: {}, final score: {}".format(dealer_card[0], dealers_current_card))

        if (players_current_card <= 21) and (dealers_current_card < players_current_card):
            print("You went over. You lose")
        elif dealers_current_card > added and added <= 21:
            print("True")
            print("You won!")
        elif added > 21 and dealers_current_card < 21:
            print("You lose, the computer won!")
        elif added < 21 and dealers_current_card > 21:
            print("You won, the computer loss!")
        elif added == dealers_current_card:
            print("It's a draw!")

    elif more_cards == "n":
        if players_current_card <= 21 and dealers_current_card < players_current_card:
            print("You went over. You lose")
        elif dealers_current_card > players_current_card and players_current_card <= 21:
            print("You won!")
        elif players_current_card > 21 and dealers_current_card < 21:
            print("You lose, the computer won!")
        elif players_current_card < 21 and dealers_current_card > 21:
            print("You won, the computer loss!")
        elif players_current_card == dealers_current_card:
            print("It's a draw!")
        
        if decision == "n":
            print("Thank you for BANKING WITH US!")
            wants_to_continue = False