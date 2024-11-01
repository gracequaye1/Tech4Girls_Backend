# Create a file named list_and_set_methods.py
# List Methods
my_list = [1, 2, 3, 4, 5]

# Append
my_list.append(6)
print("After append:", my_list)

# Remove
my_list.remove(3)
print("After remove:", my_list)

# Pop
popped_value = my_list.pop()
print("Popped value:", popped_value)
print("After pop:", my_list)

# Sort
my_list.sort()
print("After sort:", my_list)

# Reverse
my_list.reverse()
print("After reverse:", my_list)

# Extend
my_list.extend([7, 8, 9])
print("After extend:", my_list)

# Set Methods
my_set = {1, 2, 3, 4}

# Add
my_set.add(5)
print("After add:", my_set)

# Remove
my_set.remove(2)
print("After remove:", my_set)

# Union
set2 = {3, 4, 5, 6}
union_set = my_set.union(set2)
print("Union set:", union_set)

# Intersection
intersection_set = my_set.intersection(set2)
print("Intersection set:", intersection_set)

# Difference
difference_set = my_set.difference(set2)
print("Difference set:", difference_set)
