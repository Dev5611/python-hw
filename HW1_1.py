import math


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    :param radius: Radius of the circle.
    :return: Area of the circle.
    """
    return math.pi * radius ** 2


r: float = float(input("Enter the radius of the circle: "))
a: float = calculate_circle_area(r)
print("The area of the circle is:", a)
