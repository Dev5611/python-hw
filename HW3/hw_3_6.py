import re


class User:
    """
    Class representing a user with first name, last name, and email.
    Uses @property for controlled access and validation of attributes.
    """

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = None  # тимчасово None, бо перевірка через setter
        self.email = email  # виклик сеттера для перевірки формату

    #bFIRST NAME
    @property
    def first_name(self) -> str:
        """Get the user's first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Set the user's first name."""
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        self._first_name = value

    # LAST NAME
    @property
    def last_name(self) -> str:
        """Get the user's last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Set the user's last name."""
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        self._last_name = value

    # EMAIL
    @property
    def email(self) -> str:
        """Get the user's email."""
        return self._email

    @staticmethod
    def _validate_email_format(email: str) -> bool:
        """
        Validate email format using regex.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if email format is valid, False otherwise.
        """
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    @email.setter
    def email(self, value: str) -> None:
        """Set the user's email with validation."""
        if not self._validate_email_format(value):
            raise ValueError(f"Invalid email format: {value}")
        self._email = value

    # Representation-
    def repr(self) -> str:
        """Readable representation of the object."""
        return f"User(first_name='{self._first_name}', last_name='{self._last_name}', email='{self._email}')"


# Testing the User class

# Створюємо користувача
user = User("Іван", "Петренко", "ivan.petrenko@example.com")
print("User created:", user)

# Зміна імені
user.first_name = "Петро"
print("Updated first name:", user.first_name)

# Зміна прізвища
user.last_name = "Іваненко"
print("Updated last name:", user.last_name)

# Зміна email на коректний
user.email = "p.ivanenko@gmail.com"
print("Updated email:", user.email)

# Спроба встановити некоректний email
try:
    user.email = "wrong_email.com"
except ValueError as e:
    print("Error:", e)
