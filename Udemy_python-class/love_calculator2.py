name1 = input()
name2 = input()

combined = name1 + name2
lowercase = combined.lower()

t = lowercase.count('t')
r = lowercase.count('r')
u = lowercase.count('u')
e = lowercase.count('e')

first = t + r + u + e

l = lowercase.count('l')
o = lowercase.count('o')
v = lowercase.count('v')
e = lowercase.count('e')

second = l + o + v + e

result = int(str(first) + str(second))

print("The love calculator is calculating your score...")

if (result > 10) or (result > 90):
    print(f'Your Love score is {result}, you can go together like coke and mentos')

elif (result >= 40) and (result < 51):
    print(f'Your love score is {result}, you are alright together.')

else:
    print(f"Your score is {result}.")