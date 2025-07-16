print("*"*100)
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds" 

##############################################

# Function to convert days to seconds
def days_to_units(num_of_days):
    #condition = num_of_days > 0
    #print(condition)
    #print(type(condition))
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"

# Function to check if the input is valid and perform the calculation    
def check_input(input_value):
    #if user_input.isdigit():
    try:
        user_input_number = int(input_value)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0 days, which is not a valid input for this calculation.")
        else:
            print("You entered a negative number, which is not valid for this calculation.")
    #else:
    except ValueError:
        print("You entered an invalid value. Please enter a positive integer.")



#User input
user_input = ""
while user_input != "exit":
    user_input = input("Enter the number of days:\n")
    for num_of_days_element in user_input.split(","):
        check_input(num_of_days_element)


##############################################
print("*"*100)
"""

user_input_1 = input("Enter the number 1:\n")
user_input_2 = input("Enter the number 2:\n")

def add_numbers(num1, num2):
    return int(num1) + int(num2)


print(f"You entered: {add_numbers(user_input_1, user_input_2)} ")

"""