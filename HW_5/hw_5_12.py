class LoggingMeta(type):
    """
    Метаклас, який автоматично додає логування доступу до атрибутів
    для всіх класів, що його використовують.

    Кожного разу, коли атрибут читається або змінюється,
    виводиться відповідне повідомлення у консоль.
    """

    def __new__(mcs, name, bases, namespace):
        """
        Додає методи __getattribute__ та __setattr__ автоматично
        до класу, якщо вони ще не визначені.

        Args:
            name (str): Ім'я класу, що створюється.
            bases (tuple): Базові класи.
            namespace (dict): Атрибути класу.
        """
        # Перевірка, чи клас має свій __getattribute__, якщо ні — додаємо
        if "__getattribute__" not in namespace:
            def __getattribute__(self, attr_name):
                value = super(cls, self).__getattribute__(attr_name)
                print(f"Logging: accessed '{attr_name}'")
                return value
            namespace["__getattribute__"] = __getattribute__

        # Перевірка, чи клас має свій __setattr__, якщо ні — додаємо
        if "__setattr__" not in namespace:
            def __setattr__(self, attr_name, value):
                print(f"Logging: modified '{attr_name}' to '{value}'")
                super(cls, self).__setattr__(attr_name, value)
            namespace["__setattr__"] = __setattr__

        # Створюємо клас стандартним способом через type
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


# ------------------------- Приклад використання -------------------------

class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


# Створюємо об'єкт
obj = MyClass("Python")

# Читання атрибуту
print(obj.name)  # Викличе логування під час читання

# Зміна атрибуту
obj.name = "New Python"  # Викличе логування під час зміни
