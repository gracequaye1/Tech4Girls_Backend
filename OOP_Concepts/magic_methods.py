class Rectangle:
    def __init__(self, length, width):
        """Initialize the rectangle's dimensions."""
        self.length = length
        self.width = width

    @property
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    @property
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    def __eq__(self, other):
        """Compare two rectangles based on their area."""
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False


# Demonstration
# Create two rectangle instances
rect1 = Rectangle(5, 3)
rect2 = Rectangle(6, 2)

# Use the __str__ method
print(rect1)  # Output: Rectangle(Length: 5, Width: 3)
print(rect2)  # Output: Rectangle(Length: 6, Width: 2)

# Calculate and display area and perimeter
print(f"Area of rect1: {rect1.area}")  # Output: 15
print(f"Perimeter of rect1: {rect1.perimeter}")  # Output: 16

print(f"Area of rect2: {rect2.area}")  # Output: 12
print(f"Perimeter of rect2: {rect2.perimeter}")  # Output: 16

# Compare rectangles using __eq__
if rect1 == rect2:
    print("rect1 and rect2 have equal areas.")
else:
    print("rect1 and rect2 do not have equal areas.")  # Output: rect1 and rect2 do not have equal areas.
