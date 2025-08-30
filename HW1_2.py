class Rectangle:
    """Class representing a rectangle with width and height"""

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a rectangle

        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """Return True if the rectangle is a square, otherwise False"""
        return self.width == self.height

    def resize(self, new_width: float, new_height: float) -> None:
        """
        Resize the rectangle

        :param new_width: New width of the rectangle
        :param new_height: New height of the rectangle
        """
        self.width = new_width
        self.height = new_height


r = Rectangle(8, 10)
print("Area", r.area())
print("Perimeter", r.perimeter())
print("Is square?", r.is_square())

r.resize(6, 6)
print("New size:", r.width, "x", r.height)
print("Is square?", r.is_square())

