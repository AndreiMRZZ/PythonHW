# Import the abstract base class tools for defining abstract classes
from abc import ABC, abstractmethod
import math

# Define an abstract base class for shapes
class Shape(ABC):
    """
    Abstract base class for different geometric shapes.
    Requires implementation of the area() method.
    """

    # Declare an abstract method that must be implemented by subclasses
    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    """
    Represents a rectangle shape.
    Calculates area as: width * height.
    """

    # Initialize the rectangle with width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for rectangles
    def area(self):
        return self.width * self.height

# Define a Circle class that inherits from Shape
class Circle(Shape):
    """
    Represents a circle shape.
    Calculates area as: π * radius^2.
    """

    # Initialize the circle with a radius
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for circles
    def area(self):
        return math.pi * self.radius ** 2

# Main part of the program
if __name__ == "__main__":
    # Print the docstring for the Rectangle class
    print("Rectangle docstring:\n", Rectangle.__doc__)
    # Print the docstring for the Circle class
    print("\nCircle docstring:\n", Circle.__doc__)

    # Create a list of shape objects (rectangles and circles)
    shapes = [
        Rectangle(3, 4),    # Rectangle with width 3 and height 4
        Circle(5),          # Circle with radius 5
        Rectangle(6, 7),    # Rectangle with width 6 and height 7
        Circle(2.5),        # Circle with radius 2.5
        Rectangle(10, 2)    # Rectangle with width 10 and height 2
    ]

    # Initialize counters for rectangles and circles
    rect_count = 0
    circle_count = 0

    # Iterate through the list of shapes
    for shape in shapes:
        # Print the class name and area of each shape
        print(f"{shape.__class__.__name__} with area: {shape.area():.2f}")
        # Count rectangles and circles
        if isinstance(shape, Rectangle):
            rect_count += 1
        elif isinstance(shape, Circle):
            circle_count += 1

    # Print the total number of rectangles
    print(f"\nTotal Rectangles: {rect_count}")
    # Print the total number of circles
    print(f"Total Circles: {circle_count}")
