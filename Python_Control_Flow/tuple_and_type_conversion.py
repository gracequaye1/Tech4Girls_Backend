# Create a file named tuple_and_type_conversion.py
# Define a tuple
my_tuple = (1, "Hello", 3.14, True, [1, 2, 3])

# Print first and last elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Count and index methods
print("Count of 'Hello':", my_tuple.count("Hello"))
print("Index of 3.14:", my_tuple.index(3.14))

# Type conversion examples
int_to_float = float(10)  # Convert integer to float
float_to_int = int(10.5)  # Convert float to integer
str_to_int = int("42")     # Convert string to integer

# Print results
print("Integer to Float:", int_to_float)
print("Float to Integer:", float_to_int)
print("String to Integer:", str_to_int)

# Joining a list of strings
string_list = ["Join", "these", "words"]
joined_string = " ".join(string_list)
print("Joined string:", joined_string)
