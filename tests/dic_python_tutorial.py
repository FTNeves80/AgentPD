from modulos import check_input , user_input_message
from datetime import datetime

print("___"*20)
print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#User input
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(f"You entered: {days_and_unit}")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(f"You dictionary: {days_and_unit_dictionary}")
    check_input(days_and_unit_dictionary)
    print("___"*20)

