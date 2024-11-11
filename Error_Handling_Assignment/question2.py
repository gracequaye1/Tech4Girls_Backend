data = {"name": "Alice", "age": 25, "country": "Wonderland"}
key = input("Enter the key you want to look up: ")

try:
    # Try to access the key in the dictionary
    print("Value:", data[key])
except KeyError:
    # Handle the error if the key doesn't exist
    print("Error: The key you entered does not exist in the dictionary.")
