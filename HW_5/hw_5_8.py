import inspect


def analyze_inheritance(cls: type) -> None:
    """
    Аналізує клас, виводить інформацію про його базові класи
    та всі методи, успадковані від них.

    Args:
        cls (type): Клас, який потрібно проаналізувати.
    """
    print(f"Клас {cls.__name__} наслідує:\n")

    # Отримуємо базові класи (прямі батьки)
    base_classes = cls.__bases__

    if not base_classes:
        print(" - Клас не має базових класів")
        return

    # Перебираємо кожен базовий клас
    for base in base_classes:
        # Збираємо методи базового класу
        base_methods = inspect.getmembers(base, predicate=inspect.isfunction)

        if not base_methods:
            continue

        for method_name, _ in base_methods:
            # Перевіряємо, чи метод не перевизначений у дочірньому класі
            if method_name not in cls.__dict__:
                print(f" - {method_name} з {base.__name__}")
    print()


# ------------------------- Приклад використання -------------------------

class Parent:
    def parent_method(self):
        """Метод базового класу"""
        pass


class AnotherParent:
    def another_method(self):
        """Метод іншого базового класу"""
        pass


class Child(Parent, AnotherParent):
    def child_method(self):
        """Метод дочірнього класу"""
        pass


# Виклик функції аналізу
analyze_inheritance(Child)
