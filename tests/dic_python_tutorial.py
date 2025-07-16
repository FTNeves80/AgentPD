from modulos import check_input

print("___"*20)
#User input
user_input = ""
while user_input != "exit":
    user_input = input("Enter the number of days:\n")
    days_and_unit = user_input.split(":")
    print(f"You entered: {days_and_unit}")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(f"You dictionary: {days_and_unit_dictionary}")
    check_input(days_and_unit_dictionary)
    print("___"*20)
