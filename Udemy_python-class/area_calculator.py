# Write your code below this line 👇

'''
I have to import this module to round up my answer if I get 1.1 as an answer
since we cant't buy 1.1 cans of paint, it needed to be two'''
import math

def paint_calc(height, width, cover=5):
    calculation = (height * width) / cover
    # This line rounds it up if it is 0.9 or 0.1 it will still be 1 as final answer.
    result = math.ceil(calculation)
    print("You'll need {} cans of paint.".format(result))


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)