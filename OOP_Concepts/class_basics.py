class Car:
    def __init__(self, make, model, year):
        """Initialize the car's make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Display the car's details."""
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Call the display_info method
my_car.display_info()
