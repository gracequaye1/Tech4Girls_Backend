# Parent class
class Employee:
    def __init__(self, name, position):
        """Initialize name and position of the employee."""
        self.name = name
        self.position = position

    def get_details(self):
        """Display the employee's details."""
        print(f"Name: {self.name}, Position: {self.position}")

# Child class
class Manager(Employee):
    def __init__(self, name, position, department):
        """Initialize inherited and additional attributes."""
        super().__init__(name, position)  # Initialize name and position using the parent class
        self.department = department

    def get_details(self):
        """Display the manager's details, including the department."""
        super().get_details()  # Call the parent method to display name and position
        print(f"Department: {self.department}")

# Demonstration
# Create an instance of Employee
employee = Employee("Alice Johnson", "Software Engineer")
print("Employee Details:")
employee.get_details()

# Create an instance of Manager
manager = Manager("Grace Okailey Quaye", "Team Manager", "Marketing")
print("\nManager Details:")
manager.get_details()

