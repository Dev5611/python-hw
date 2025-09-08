import math
from typing import List


class Vector:
    """
    Class to represent a mathematical vector in 2D or 3D space.

    Supports:
    - Addition (add)
    - Subtraction (sub)
    - Multiplication by a number (mul)
    - Comparison by length (lt, eq)
    - Length calculation (length method)
    """

    def __init__(self, components: List[float]) -> None:
        """Initialize vector with a list of numeric components."""
        self.components = components

    def __add__(self, other: "Vector") -> "Vector":
        """Vector addition: element-wise."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition")
        new_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(new_components)

    def __sub__(self, other: "Vector") -> "Vector":
        """Vector subtraction: element-wise."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for subtraction")
        new_components = [a - b for a, b in zip(self.components, other.components)]
        return Vector(new_components)

    def __mul__(self, scalar: float) -> "Vector":
        """Multiply vector by a scalar (number)."""
        new_components = [a * scalar for a in self.components]
        return Vector(new_components)

    def __lt__(self, other: "Vector") -> bool:
        """Compare vectors by length: self < other."""
        return self.length() < other.length()

    def __eq__(self, other: "Vector") -> bool:
        """Check if vectors are equal by their components."""
        return self.components == other.components

    def length(self) -> float:
        """Calculate vector length using the Euclidean norm."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def __repr__(self) -> str:
        """String representation of vector."""
        return f"Vector({self.components})"


# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1:", v1)
print("v2:", v2)

# Addition
print("v1 + v2 =", v1 + v2)  # Vector([5, 7, 9])

# Subtraction
print("v1 - v2 =", v1 - v2)  # Vector([-3, -3, -3])

# Multiplication by scalar
print("v1 * 2 =", v1 * 2)  # Vector([2, 4, 6])

# Lengths
print("Length of v1 =", v1.length())  # 3.7416573867739413
print("Length of v2 =", v2.length())  # 8.774964387392123

# Comparisons
print("v1 < v2:", v1 < v2)  # True
print("v1 == v2:", v1 == v2)  # False
