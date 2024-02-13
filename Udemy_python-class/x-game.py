line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Don't change the code above
# Write your code below this row

# This stores the first character entered by the user in the variable called letter
# and makes it lowercase, so irrespective of the manner the user writes the letter a,b and c, 
# it does not aftet our code.
letter = position[0].lower()
desired_letter = position[-1]
# This is serves as a sample for the input from the user in the position[0]. i.e. index 0.
abc = ['a', 'b', 'c'] # So here, the character gotten from letter at the position of 
# [0] most be a,b or c, then we check for the letter in abc list and match it with the
# index of the letter in abc variable or list.
# This checks for the index at which the letters occur and match it with the a, b or c.
# Which in this case may be 0, 1 or two since it's just three characters.
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = desired_letter

print(f"{line1}\n{line2}\n{line3}")
