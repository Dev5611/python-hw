from types import FunctionType
from typing import Dict, Callable


def create_class(class_name: str, methods: Dict[str, Callable]) -> type:
    """
    Динамічно створює клас із заданим ім'ям та методами.

    Args:
        class_name (str): Назва нового класу.
        methods (Dict[str, Callable]): Словник методів у форматі {назва: функція}.

    Returns:
        type: Новий клас, створений динамічно.

    Raises:
        TypeError: Якщо будь-яке значення у словнику не є функцією.
    """
    # Перевіряємо, що всі значення в словнику — це функції
    for name, func in methods.items():
        if not isinstance(func, FunctionType):
            raise TypeError(f"Метод '{name}' повинен бути функцією, отримано {type(func)}")

    # Створюємо новий клас динамічно
    # Аргументи type():
    # 1. Ім'я класу
    # 2. Базові класи (тут порожній кортеж, бо не наслідуємо інші класи)
    # 3. Словник атрибутів і методів
    new_class = type(class_name, (), methods)

    return new_class


# ------------------------- Приклад методів -------------------------

def say_hello(self) -> str:
    """Повертає привітання."""
    return "Hello!"


def say_goodbye(self) -> str:
    """Повертає прощання."""
    return "Goodbye!"


def greet_personal(self, name: str) -> str:
    """Повертає персональне привітання."""
    return f"Hello, {name}!"


# Словник із методами, які будуть додані до класу
methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye,
    "greet_personal": greet_personal
}

# ------------------------- Створення динамічного класу -------------------------

MyDynamicClass = create_class("MyDynamicClass", methods)

# Створюємо екземпляр динамічно створеного класу
obj = MyDynamicClass()

# Використання методів нового класу
print(obj.say_hello())         # Hello!
print(obj.say_goodbye())       # Goodbye!
print(obj.greet_personal("Alex"))  # Hello, Alex!
