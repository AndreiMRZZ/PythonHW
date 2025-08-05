from abc import ABC, abstractmethod
import math

#abstract base class for shapes
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    
    print("Rectangle docstring:\n", Rectangle.__doc__)
    print("\nCircle docstring:\n", Circle.__doc__)

    shapes = [
        Rectangle(3, 4),    
        Circle(5),          
        Rectangle(6, 7),    
        Circle(2.5),       
        Rectangle(10, 2)    
    ]

    rect_count = 0
    circle_count = 0

    for shape in shapes:
        print(f"{shape.__class__.__name__} with area: {shape.area():.2f}")
        if isinstance(shape, Rectangle):
            rect_count += 1
        elif isinstance(shape, Circle):
            circle_count += 1

    print(f"\nTotal Rectangles: {rect_count}")
    print(f"Total Circles: {circle_count}")
