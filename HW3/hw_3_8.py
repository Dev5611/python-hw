class Price:
    """
    Class representing a product price with automatic rounding to two decimals.

    Supports:
    - Addition (add)
    - Subtraction (sub)
    - Comparison (eq, lt, gt)
    """

    def __init__(self, amount: float) -> None:
        """
        Initialize a price with rounding to two decimals.

        Args:
            amount (float): The price amount.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Price cannot be negative")
        self.amount = round(amount, 2)

    # Addition
    def __add__(self, other: "Price") -> "Price":
        """
        Add two Price objects and return a new Price.
        """
        if not isinstance(other, Price):
            return NotImplemented
        return Price(self.amount + other.amount)

    # Subtraction
    def __sub__(self, other: "Price") -> "Price":
        """
        Subtract one Price from another and return a new Price.
        Result cannot be negative.
        """
        if not isinstance(other, Price):
            return NotImplemented
        if self.amount < other.amount:
            raise ValueError("Resulting price cannot be negative")
        return Price(self.amount - other.amount)

    # Comparisons
    def __eq__(self, other: object) -> bool:
        """
        Check if two prices are equal.
        """
        if not isinstance(other, Price):
            return False
        return self.amount == other.amount

    def __lt__(self, other: "Price") -> bool:
        """
        Check if this price is less than another.
        """
        return self.amount < other.amount

    def __gt__(self, other: "Price") -> bool:
        """
        Check if this price is greater than another.
        """
        return self.amount > other.amount

    # Representation
    def __repr__(self) -> str:
        """
        Developer-friendly string representation of the Price object.
        """
        return f"Price({self.amount:.2f})"

    def __str__(self) -> str:
        """
        User-friendly string format for displaying prices.
        """
        return f"${self.amount:.2f}"

    # Classmethod for alternative creation
    @classmethod
    def from_cents(cls, cents: int) -> "Price":
        """
        Alternative constructor to create a Price from cents.

        Args:
            cents (int): Amount in cents.

        Raises:
            ValueError: If cents is negative.
        """
        if cents < 0:
            raise ValueError("Cents cannot be negative")
        return cls(cents / 100)


# Testing the Price class

# Створюємо ціни
p1 = Price(19.999)  # автоматично округлюється до $20.00
p2 = Price(5.50)
p3 = Price(25.50)

print("p1 =", p1)  # $20.00
print("p2 =", p2)  # $5.50
print("p3 =", p3)  # $25.50

# Додавання
total = p1 + p2
print("p1 + p2 =", total)  # $25.50

# Віднімання
diff = p3 - p2
print("p3 - p2 =", diff)   # $20.00

# Порівняння
print("p1 == p2:", p1 == p2)  # False
print("p1 < p3:", p1 < p3)    # True
print("p3 > p2:", p3 > p2)    # True

# Створення з центів
p4 = Price.from_cents(999)
print("Price from cents 999 =", p4)  # $9.99

# Демонстрація помилки при від'ємному результаті
try:
    invalid = p2 - p3
except ValueError as e:
    print("Error:", e)
