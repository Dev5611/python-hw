# python-hw

````markdown
# HW1: Circle and Rectangle

## Description

This repository contains two Python practice programs for basic geometry calculations:

1. **HW1_1.py** — calculates the area of a circle given a radius.
2. **HW1_2.py** — defines a `Rectangle` class with methods to calculate area, perimeter, check if it's a square, and resize the rectangle.

Both programs include **type annotations**, **docstrings**, and are written according to **PEP 8** standards.

---

## Usage

### HW1_1.py (Circle Area)

This program asks the user to input the radius of a circle and calculates its area.

**How to run:**

```bash
python HW1_1.py
````

**Example:**

```
Enter the radius of the circle: 5
The area of the circle is: 78.53981633974483
```

**Notes:**

* If a negative radius is entered, the program will print an error and exit.
* The area is calculated using the formula: `area = π * radius^2`.

---

### HW1\_2.py (Rectangle)

This program defines a `Rectangle` class and demonstrates its usage.

**Class methods:**

* `area()` — returns the area of the rectangle.
* `perimeter()` — returns the perimeter of the rectangle.
* `is_square()` — returns `True` if width equals height, otherwise `False`.
* `resize(new_width, new_height)` — changes the rectangle's width and height.

**How to run:**

```bash
python HW1_2.py
```

**Example output:**

```
Area: 80
Perimeter: 36
Is square? False
New size: 6 x 6
Is square? True
```

## Files

* `HW1_1.py` — Calculates the area of a circle with user input.
* `HW1_2.py` — `Rectangle` class with methods and test code.
* `README.md` — Project documentation.

## Requirements

* Python 3.6 or higher
* No additional libraries are required (only standard library `math` and `sys` are used).

## Notes

* Both programs include docstrings and type annotations for better readability and maintainability.
* Code follows PEP 8 style guidelines.
