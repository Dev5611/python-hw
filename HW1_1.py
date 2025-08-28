import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

r = float(input("Enter the radius of the circle: "))
a = calculate_circle_area(r)
print("The area of the circle is: ", a)
