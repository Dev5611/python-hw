class LimitedAttributesMeta(type):
    """
    Метаклас, який обмежує кількість атрибутів у класі.

    Якщо клас містить більше, ніж дозволену кількість атрибутів,
    піднімається помилка TypeError.
    """
    MAX_ATTRIBUTES = 3  # Максимальна кількість дозволених атрибутів

    def __new__(mcs, name, bases, namespace):
        """
        Перевіряє кількість атрибутів під час створення класу.

        Args:
            name (str): Назва класу.
            bases (tuple): Базові класи.
            namespace (dict): Атрибути, визначені в класі.

        Raises:
            TypeError: Якщо кількість атрибутів перевищує ліміт.
        """
        # Відфільтровуємо службові атрибути (__init__, __module__, __dict__ тощо)
        user_attributes = [
            attr for attr in namespace.keys() if not attr.startswith("__")
        ]

        if len(user_attributes) > mcs.MAX_ATTRIBUTES:
            raise TypeError(
                f"Клас {name} не може мати більше {mcs.MAX_ATTRIBUTES} атрибутів. "
                f"Зараз є: {len(user_attributes)}"
            )

        return super().__new__(mcs, name, bases, namespace)


# ------------------------- Приклад використання -------------------------

class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Розкоментуйте цей рядок, щоб побачити помилку


# Створення екземпляра працює нормально, якщо атрибутів не більше 3
obj = LimitedClass()
print("Об'єкт створено успішно:", obj)
