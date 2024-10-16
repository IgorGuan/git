import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

    def compare_area(self, other_shape):
        if self.area() > other_shape.area():
            return "greater than"
        elif self.area() < other_shape.area():
            return "less than"
        else:
            return "equal to"

    def compare_perimeter(self, other_shape):
        if self.perimeter() > other_shape.perimeter():
            return "greater than"
        elif self.perimeter() < other_shape.perimeter():
            return "less than"
        else:
            return "equal to"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assuming it's an equilateral triangle for simplicity
        return 3 * self.base  # This is a simplification


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# for example
if __name__ == "__main__":
    square = Square(4)
    rectangle = Rectangle(3, 6)
    triangle = Triangle(4, 3)
    circle = Circle(5)
    print(f"Square area: {square.area()}, perimeter: {square.perimeter()}")
    print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
    print(f"Triangle area: {triangle.area()}, perimeter: {triangle.perimeter()}")
    print(f"Circle area: {circle.area()}, perimeter: {circle.perimeter()}")
    # square 
    print(f"Square area is {square.compare_area(rectangle)} Rectangle area.")
    print(f"Circle area is {circle.compare_area(triangle)} Triangle area.")
    # perimeter
    print(f"Rectangle perimeter is {rectangle.compare_perimeter(circle)} Circle perimeter.")
    print(f"Triangle perimeter is {triangle.compare_perimeter(square)} Square perimeter.")
