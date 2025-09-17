def analyze_object(obj: object) -> None:
    """
    Analyze any Python object and display:
      - The object's type.
      - A list of all attributes and methods.
      - The type of each attribute or method.

    Args:
        obj (object): The object to analyze.
    """
    # Виводимо тип об'єкта
    print(f"Тип об'єкта: {type(obj)}\n")

    # Отримуємо список атрибутів та методів
    attributes = dir(obj)
    print("Атрибути і методи:")

    for attr in attributes:
        try:
            value = getattr(obj, attr)  # отримуємо значення атрибуту
            print(f"- {attr}: {type(value)}")
        except Exception:
            # На випадок, якщо доступ до атрибуту викликає помилку
            print(f"- {attr}: <невідомий тип>")

    print("\n")  # Відступ для зручності


# ------------------------- Приклад використання -------------------------

class MyClass:
    """Клас з прикладом для аналізу."""
    def __init__(self, value: str) -> None:
        self.value = value

    def say_hello(self) -> str:
        return f"Hello, {self.value}"


obj = MyClass("World")

# Викликаємо функцію аналізу
analyze_object(obj)
