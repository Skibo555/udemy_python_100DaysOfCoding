print("Welcome to the tip calculator.\nWhat was the total bill? $ ")
total_bill = float(input())

percentage_to_be_shared = int(input("What percentage (%) tip would you like to give? 10, 12, or 15? "))

people_to_split = int(input("How many people to split the bill? "))

result = (percentage_to_be_shared / total_bill) * total_bill

# percentage = round(result * 100, 2)

print("Each person should pay: ${}". format(result))