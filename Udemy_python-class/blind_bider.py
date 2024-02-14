from biders_art import logo
print(logo)

bidder_data = {}
flag = True

def highest_bidder(bidder_data):
    higest_bid = 0
    winner = ''
    for bidders in bidder_data:
        amount = bidder_data[bidders]
        if amount > higest_bid:
            higest_bid = amount
            winner = bidders
    print("The winner is {} with the bid of ${}.".format(winner, higest_bid))
    return winner

while flag:
    bidder_name = input("What is you name? ")
    bid_amount = int(input("How much are you welling to pay? $"))
    bidder_data[bidder_name] = bid_amount
    done = input("Are there more didders? Type 'yes' or 'no' ").lower()
    if done == 'no':
        flag = False
        highest_bidder(bidder_data)
    elif done == 'yes':
        flag = True
    else:
        flag = False
        print("You've entered a wrong response!")
