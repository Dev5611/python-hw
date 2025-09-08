class Fraction:
    """
    Class to represent fractions (rational numbers).

    Supports:
    - addition (add)
    - subtraction (sub)
    - multiplication (mul)
    - division (truediv)
    Also implements repr for nice display like "numerator/denominator".
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: "Fraction") -> "Fraction":
        """Addition of two fractions."""
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtraction of two fractions."""
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiplication of two fractions."""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Division of two fractions."""
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator 0")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __repr__(self) -> str:
        """String representation in 'numerator/denominator' format."""
        return f"{self.numerator}/{self.denominator}"


# Example usage
f1 = Fraction(1, 2)   # 1/2
f2 = Fraction(3, 4)   # 3/4

print("f1:", f1)
print("f2:", f2)

print("Addition:", f1 + f2)       # 1/2 + 3/4 = 10/8
print("Subtraction:", f1 - f2)    # 1/2 - 3/4 = -2/8
print("Multiplication:", f1 * f2) # 1/2 * 3/4 = 3/8
print("Division:", f1 / f2)       # 1/2 ÷ 3/4 = 4/6
