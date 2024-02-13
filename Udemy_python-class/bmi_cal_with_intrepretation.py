print("Please enter your weight")
weight = float(input())
print("What is your height?")
height = float(input())

bmi = round(weight / (height**2), 2)

# The conditional statements goes here.

if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight.")
elif bmi > 24.9 and bmi <= 25:
    print(f"Your BMI is {bmi}, and you have a normal weight.")
elif bmi >= 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, and you are slightly overweight.")
elif bmi == 30 and bmi < 35:
    print(f"Your BMI is {bmi}, and you are obese")
elif bmi > 35:
    print(f"Your BMI is {bmi}, and you are clinically obese.")