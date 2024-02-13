print("Please enter your weight")
weight = float(input())
print("What is your height?")
height = float(input())

bmi = round(weight / (height**2), 2)
print(bmi)