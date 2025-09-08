import math
from typing import List


class Vector:
    """
    Class representing a mathematical vector in n-dimensional space.

    Supports:
    - Addition (add)
    - Subtraction (sub)
    - Dot product (mul)
    - Comparison by length (lt, eq, gt)
    """

    def __init__(self, components: List[float]) -> None:
        """
        Initialize the vector.

        Args:
            components (List[float]): List of numeric components of the vector.
        """
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = components

    # Vector Addition
    def __add__(self, other: "Vector") -> "Vector":
        """Element-wise addition of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        new_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(new_components)

    # Vector Subtraction
    def __sub__(self, other: "Vector") -> "Vector":
        """Element-wise subtraction of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction")
        new_components = [a - b for a, b in zip(self.components, other.components)]
        return Vector(new_components)

    # Dot Product
    def __mul__(self, other: "Vector") -> float:
        """Calculate the dot product of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

    # ector Length
    def length(self) -> float:
        """Calculate the Euclidean length (magnitude) of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    # Comparison by length
    def __lt__(self, other: "Vector") -> bool:
        """Compare vectors by length: self < other."""
        return self.length() < other.length()

    def __eq__(self, other: "Vector") -> bool:
        """Check if two vectors are equal by components."""
        return self.components == other.components

    def __gt__(self, other: "Vector") -> bool:
        """Compare vectors by length: self > other."""
        return self.length() > other.length()

    # Representation
    def __repr__(self) -> str:
        """Readable string representation."""
        return f"Vector({self.components})"


# Testing the Vector class

# Створення векторів у 3D
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([1, 2, 3])  # для перевірки рівності

print("v1:", v1)
print("v2:", v2)

# Додавання
print("v1 + v2 =", v1 + v2)  # Vector([5, 7, 9])

# Віднімання
print("v1 - v2 =", v1 - v2)  # Vector([-3, -3, -3])

# Скалярний добуток
print("v1 * v2 =", v1 * v2)  # 1*4 + 2*5 + 3*6 = 32

# Довжини
print("Length of v1 =", v1.length())  # 3.7416573867739413
print("Length of v2 =", v2.length())  # 8.774964387392123

# Порівняння
print("v1 < v2:", v1 < v2)   # True
print("v1 == v2:", v1 == v2) # False
print("v1 == v3:", v1 == v3) # True
print("v2 > v1:", v2 > v1)   # True
