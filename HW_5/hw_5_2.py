def call_function(obj: object, method_name: str, *args):
    """
    Dynamically call a method on an object by its name.

    Args:
        obj (object): The object on which to call the method.
        method_name (str): The name of the method to call.
        *args: Arguments to pass to the method.

    Returns:
        Any: The result of the method call.

    Raises:
        AttributeError: If the object has no method with the given name.
        TypeError: If the attribute exists but is not callable.
    """
    # Перевіряємо, чи атрибут існує
    if not hasattr(obj, method_name):
        raise AttributeError(f"Object {obj} has no method '{method_name}'")

    method = getattr(obj, method_name)

    # Перевіряємо, чи метод викликається
    if not callable(method):
        raise TypeError(f"Attribute '{method_name}' of {obj} is not callable")

    return method(*args)


# ------------------------- Приклад використання -------------------------

class Calculator:
    """Простий калькулятор."""
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b


calc = Calculator()

# Викликаємо методи динамічно
print(call_function(calc, "add", 10, 5))       # 15
print(call_function(calc, "subtract", 10, 5))  # 5
