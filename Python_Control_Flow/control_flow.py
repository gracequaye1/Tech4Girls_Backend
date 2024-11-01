# Create a file named control_flow.py
# Ask user for their age
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")


