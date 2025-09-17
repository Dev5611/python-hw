class TypeCheckedMeta(type):
    """
    Метаклас, який перевіряє типи атрибутів під час їх встановлення
    згідно з анотаціями класу.

    Якщо тип значення не відповідає типовому опису,
    піднімається помилка TypeError.
    """

    def __new__(mcs, name, bases, namespace):
        """
        Додає в клас перевірку типів для атрибутів.

        Args:
            name (str): Назва класу.
            bases (tuple): Базові класи.
            namespace (dict): Атрибути, визначені в класі.

        Returns:
            type: Новий клас з перевіркою типів.
        """
        annotations = namespace.get('__annotations__', {})

        # Якщо в класі вже є свій __setattr__, не змінюємо його
        original_setattr = namespace.get('__setattr__')

        def __setattr__(self, attr_name, value):
            """Перевірка типів при встановленні значення атрибуту."""
            if attr_name in annotations:
                expected_type = annotations[attr_name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Для атрибута '{attr_name}' очікується тип "
                        f"'{expected_type.__name__}', але отримано "
                        f"'{type(value).__name__}'."
                    )
            # Виклик оригінального __setattr__ або стандартного
            if original_setattr:
                original_setattr(self, attr_name, value)
            else:
                super(cls, self).__setattr__(attr_name, value)

        namespace['__setattr__'] = __setattr__

        # Створюємо новий клас стандартним способом
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


# ------------------------- Приклад використання -------------------------

class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


# Створюємо об'єкт класу
p = Person()

# Коректне присвоєння
p.name = "John"   # Все добре
p.age = 25        # Все добре

print(p.name, p.age)  # John 25

# Некоректне присвоєння
try:
    p.age = "30"  # Викличе помилку
except TypeError as e:
    print(e)
