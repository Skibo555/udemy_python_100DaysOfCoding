year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year {} is a leap year.".format(year))

else:
    print("The year {} is not a leap year.".format(year))