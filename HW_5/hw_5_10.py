class SingletonMeta(type):
    """
    Метаклас, який реалізує патерн Singleton.
    Дозволяє створити лише один екземпляр класу.

    Якщо екземпляр уже створений — повертає його замість створення нового.
    """
    _instances = {}  # Словник для збереження екземплярів класів

    def __call__(cls, *args, **kwargs):
        """
        Перевизначає виклик класу.
        Перевіряє, чи є вже створений екземпляр, і повертає його,
        якщо він існує, інакше створює новий.
        """
        if cls not in cls._instances:
            # Викликаємо стандартну логіку створення нового об'єкта
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# ------------------------- Приклад використання -------------------------

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


# Створюємо два об'єкти
obj1 = Singleton()  # Виведе "Creating instance"
obj2 = Singleton()  # Не створить новий екземпляр

# Перевіряємо, чи це один і той самий об'єкт
print(obj1 is obj2)  # True
