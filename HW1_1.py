import math
import sys


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle

    :param radius: Radius of the circle
    :return: Area of the circle
    """
    return math.pi * radius ** 2


def main() -> None:
    """Ask the user for a radius and print the area of the circle"""
    r: float = float(input("Enter the radius of the circle: "))

    if r < 0:
        print("Error: Radius cannot be negative.")
        sys.exit()

    a: float = calculate_circle_area(r)
    print("The area of the circle is:", a)
