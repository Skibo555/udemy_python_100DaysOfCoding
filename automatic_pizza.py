print("Thank you for choosing Python Deliveries!")
size = input("What size of pizza do you want? S, M or L ")
pepperoni = input("Do you want to add pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 's' or 'S':
    bill = 15
    if pepperoni == 'y' or 'Y':
        bill = +2
        if cheese == 'y' or 'Y':
            bill =+ 3
            print('Your final bill is ${}.'.format(bill))
    else:
        print('Your final bill is ${}.'.format(bill))
    if cheese == 'y' or 'Y':
        bill =+ 3
        print('Your final bill is ${}.'.format(bill))
    else:
        print('Your final bill is ${}.'.format(bill))
elif size == 'm' or 'M':
    bill = 20
    if pepperoni == 'y' or 'Y':
        bill =+ 2
        if cheese == 'y' or 'Y':
            bill =+ 3
            print('Your final bill is ${}.'.format(bill))
    else:
        print('Your final bill is ${}.'.format(bill))
    if cheese == 'y' or 'Y':
        bill =+ 3
        print('Your final bill is ${}.'.format(bill))
    else:
        print('Your final bill is ${}.'.format(bill))  
elif size == 'l' or 'L':
    bill = 25
    if pepperoni == 'y' or 'Y':
        bill = +2
        if cheese == 'y' or 'Y':
            bill =+ 3
            print('Your final bill is ${}.'.format(bill))
    else:
        print('Your final bill is ${}.'.format(bill))
    if cheese == 'y' or 'Y':
        bill =+ 3
        print('Your final bill is ${}.'.format(bill))
    else:
        print('Your final bill is ${}.'.format(bill))
