print("*"*100)
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds" 

##############################################

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"

my_var = input("Enter the number of days:\n")

text = days_to_units(int(my_var))

print(text)

##############################################
"""
print("*"*100)

user_input_1 = input("Enter the number 1:\n")
user_input_2 = input("Enter the number 2:\n")

def add_numbers(num1, num2):
    return int(num1) + int(num2)


print(f"You entered: {add_numbers(user_input_1, user_input_2)} ")

"""