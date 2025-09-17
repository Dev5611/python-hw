from functools import wraps
from typing import Callable


def log_methods(cls: type) -> type:
    """
    Класовий декоратор, який логуватиме виклики всіх методів класу.
    Для кожного методу виводить його назву та аргументи.

    Args:
        cls (type): Клас, методи якого потрібно обгорнути.

    Returns:
        type: Модифікований клас з обгорнутими методами.
    """

    def log_decorator(method: Callable) -> Callable:
        """Декоратор для логування окремого методу."""
        @wraps(method)
        def wrapper(*args, **kwargs):
            print(f"Logging: {method.__name__} called with {args[1:]}, {kwargs}")
            return method(*args, **kwargs)
        return wrapper

    # Перебираємо атрибути класу та обгортаємо тільки методи
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, log_decorator(attr_value))

    return cls


# ------------------------- Приклад використання -------------------------

@log_methods
class MyClass:
    """Простий клас для демонстрації роботи декоратора log_methods."""

    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b


# Створюємо екземпляр класу
obj = MyClass()

# Виклик методів
obj.add(5, 3)        # Logging: add called with (5, 3), {}
obj.subtract(10, 4)  # Logging: subtract called with (10, 4), {}
obj.multiply(6, 7)   # Logging: multiply called with (6, 7), {}
