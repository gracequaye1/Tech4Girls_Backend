items = ["apple", "banana", "cherry"]

try:
    # Ask the user for an index
    index = int(input("Enter the index of the item you want to access: "))
    
    # Try to access the item at the provided index
    print("You selected:", items[index])

# Handle invalid integer input
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Handle index out of range
except IndexError:
    print("Index out of range. Please enter an index between 0 and", len(items) - 1)
