class BinaryNumber:
    """
    Class to represent a binary number and perform bitwise operations:
    - AND (and)
    - OR (or)
    - XOR (xor)
    - NOT (invert)
    """

    def __init__(self, value: int) -> None:
        """
        Initialize BinaryNumber with an integer value.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.value = value

    def __and__(self, other: "BinaryNumber") -> "BinaryNumber":
        """Bitwise AND operation."""
        return BinaryNumber(self.value & other.value)

    def __or__(self, other: "BinaryNumber") -> "BinaryNumber":
        """Bitwise OR operation."""
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other: "BinaryNumber") -> "BinaryNumber":
        """Bitwise XOR operation."""
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self) -> "BinaryNumber":
        """Bitwise NOT operation."""
        # обмежуємося 8 бітами для наочності
        mask = 0b11111111  # 255 у десятковій системі
        return BinaryNumber(~self.value & mask)

    def __repr__(self) -> str:
        """Readable representation in binary format."""
        return f"BinaryNumber({bin(self.value)})"

    def __to_decimal__(self) -> int:
        """Convert binary value to decimal integer."""
        return self.value

    # Testing BinaryNumber class

# Створюємо два двійкових числа
a = BinaryNumber(0b1010)  # 10 у десятковій
b = BinaryNumber(0b1100)  # 12 у десятковій

print("a:", a)  # BinaryNumber(0b1010)
print("b:", b)  # BinaryNumber(0b1100)

# AND
print("AND (a & b):", a & b)  # 0b1000 -> 8

# OR
print("OR (a | b):", a | b)  # 0b1110 -> 14

# XOR
print("XOR (a ^ b):", a ^ b)  # 0b0110 -> 6

# NOT
print("NOT (~a):", ~a)  # обертає біти у межах 8 біт
