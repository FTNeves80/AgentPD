# Function to convert days to other time units
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Invalid unit"

# Function to check if the input is valid and perform the calculation    
def check_input(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0 days, which is not a valid input for this calculation.")
        else:
            print("You entered a negative number, which is not valid for this calculation.")
    except ValueError:
        print("You entered an invalid value. Please enter a positive integer.")


user_input_message = "Enter the number of days:\n"