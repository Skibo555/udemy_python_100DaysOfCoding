f_name = input("What is your first name? ").title()
l_name = input("Your last name? ").title()

def format_name(f_name, l_name):
    full_name = f_name + " " +l_name
    print(full_name)


format_name(f_name, l_name)