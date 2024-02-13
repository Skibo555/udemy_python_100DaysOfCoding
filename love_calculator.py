name1 = input()
name2 = input()

letter1 = 't'
letter2 = 'r'
letter3 = 'u'
letter4 = 'e'

letter5 = 'l'
letter6 = 'o'
letter7 = 'v'
letter8 = 'e'

# Checking for the  characters in the first name 
can_marry1 = 0
if name1.count(letter1):
    can_marry1 += 1
if name1.count(letter2):
    can_marry1 += 1
if name1.count(letter3):
    can_marry1 += 1
if name1.count(letter4):
    can_marry1 += 1
if name1.count(letter5):
    can_marry1 += 1
if name1.count(letter6):
    can_marry1 += 1
if name1.count(letter7):
    can_marry1 += 1
if name1.count(letter8):
    can_marry1 += 1
# Checking for the  characters in the second name 

can_marry2 = 0
if name2.count(letter1):
    can_marry2 += 1
if name2.count(letter2):
    can_marry2 += 1
if name2.count(letter3):
    can_marry2 += 1
if name2.count(letter4):
    can_marry2 += 1
if name2.count(letter5):
    can_marry2 += 1
if name2.count(letter6):
    can_marry2 += 1
if name2.count(letter7):
    can_marry2 += 1
if name2.count(letter8):
    can_marry2 += 1

print("The love calculator is calculating your score...")
print(f'Your score is {can_marry1}{can_marry2}')