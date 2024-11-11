user_input = input("Enter a number: ")

try:
    # Try to convert the input to an integer
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)
except ValueError:
    # Handle the error if the input is not a valid integer
    print("Error: The input you entered is not a valid integer. Please enter a whole number.")
