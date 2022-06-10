from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    # create a set of the individual values in the list entered by the user; duplicates will be combined
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    validate_and_execute(days_and_units_dictionary)
