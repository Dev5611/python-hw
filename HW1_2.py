class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


r = Rectangle(4, 5)
print("Area", r.area())
print("Perimeter", r.perimeter())
print("Is square?", r.is_square())

r.resize(6, 6)
print("New size:", r.width, "x", r.height)
print("Is square?", r.is_square())