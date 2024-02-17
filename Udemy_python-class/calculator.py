from calculator_art import logo

print(logo)


# Function of the calculator


# ADD
def add(n1, n2):
    return n1 + n2

# SUBTRACTION

def subtract(num1, num2):
    return num1 - num2

# MULTIPLICATION

def multiply(number1, number2):
    return number1 * number2

# DIVISION

def division(number_1, number_2):
    return number_1 / number_2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': division
    }

def calculator():
    num1 = float(input("What is your first number?: "))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:

        operation_sign = input("Pick an operation from the ones above: ")

        num2 = float(input("What is your second number?: "))

        calculation_function = operations[operation_sign]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
            operation_sign = input("Pick another operation: ")
            num3 = int(input("What's the next number?: "))

            calculation_function = operations[operation_sign]
            answer2 = calculation_function(answer, num3)

            print(f"{answer} {operation_sign} {num3} = {answer2}")

        else:
            should_continue = False
            calculator()

calculator()