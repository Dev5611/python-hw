class Proxy:
    """
    Клас Proxy, який перехоплює виклики методів переданого об'єкта
    та логує їх перед передачею управління оригінальному методу.

    Args:
        target (object): Об'єкт, методи якого будуть викликатись через Proxy.
    """

    def __init__(self, target: object) -> None:
        self._target = target

    def __getattr__(self, name: str):
        """
        Перехоплює доступ до атрибутів, яких немає у Proxy,
        і намагається знайти їх у цільовому об'єкті.

        Args:
            name (str): Назва методу чи атрибуту.

        Returns:
            callable або будь-яке інше значення з оригінального об'єкта.
        """
        # Отримуємо атрибут оригінального об'єкта
        attr = getattr(self._target, name)

        # Якщо атрибут — викликаємий (метод), створюємо обгортку
        if callable(attr):
            def wrapper(*args, **kwargs):
                print(f"Calling method:\n{name} with args: {args}")
                if kwargs:
                    print(f"With keyword arguments: {kwargs}")
                return attr(*args, **kwargs)

            return wrapper

        # Якщо це звичайний атрибут — повертаємо його напряму
        return attr


# ------------------------- Приклад використання -------------------------

class MyClass:
    """Простий клас для демонстрації роботи Proxy."""

    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

    def add(self, a: int, b: int) -> int:
        return a + b


# Створюємо екземпляр оригінального класу
obj = MyClass()

# Обгортаємо його в Proxy
proxy = Proxy(obj)

# Виклик методів через Proxy
print(proxy.greet("Alice"))  # Hello, Alice!
print()
print(proxy.add(10, 5))  # 15
