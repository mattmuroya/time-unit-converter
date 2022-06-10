def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days is {num_of_days * 24} hours."
    elif conversion_unit == "minutes":
        return f"{num_of_days} days is {num_of_days * 24 * 60} minutes."
    else:
        return "Unsupported unit."


def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])  # taken from global scope
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number <= 0:
            print("Please enter a number greater than 0.")
    except ValueError:  # specify ValueError type
        print("Input invalid. Please try again.")

user_input_message = "Hi! Please enter the number of days and conversion unit in the format: '<days>:<unit>'\n"