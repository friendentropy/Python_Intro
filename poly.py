import math


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


def calculate_totalarea(shapes):
    totalarea = 0
    for shape in shapes:
        totalarea += shape.calculate_area()
        return totalarea


mycircle = Circle(9)
myrectangle = Rectangle(5, 7)
print(f"Area of circle is {mycircle.calculate_area()}")
print(f"Area of rectangle is {myrectangle.calculate_area()}")
