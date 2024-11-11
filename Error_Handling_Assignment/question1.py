try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Attempt to perform the division
    result = numerator / denominator
    print("The result is:", result)

except ValueError:
    # This block catches non-integer inputs
    print("Error: Please enter valid integers for both numerator and denominator.")

except ZeroDivisionError:
    # This block catches division by zero
    print("Error: The denominator cannot be zero. Please enter a non-zero denominator.")
