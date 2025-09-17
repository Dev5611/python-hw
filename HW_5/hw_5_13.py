class AutoMethodMeta(type):
    """
    Метаклас, який автоматично генерує методи геттера та сеттера
    для кожного атрибута класу, що не є службовим.

    - Для атрибуту 'name' створюються методи:
        get_name(self) -> повертає значення
        set_name(self, value) -> встановлює значення
    """

    def __new__(mcs, name, bases, namespace):
        """
        Автоматично додає методи геттера та сеттера для кожного
        звичайного атрибута класу.

        Args:
            name (str): Назва класу.
            bases (tuple): Базові класи.
            namespace (dict): Атрибути класу.
        """

        def make_getter(attr_name):
            """Створює геттер для атрибута."""
            def getter(self):
                return getattr(self, attr_name)
            return getter

        def make_setter(attr_name):
            """Створює сеттер для атрибута."""
            def setter(self, value):
                setattr(self, attr_name, value)
            return setter

        # Створюємо копію словника, щоб уникнути змін під час ітерації
        attributes = [
            attr for attr in namespace.keys() if not attr.startswith("__")
        ]

        for attr in attributes:
            # Якщо методів ще немає — додаємо їх
            getter_name = f"get_{attr}"
            setter_name = f"set_{attr}"

            if getter_name not in namespace:
                namespace[getter_name] = make_getter(attr)

            if setter_name not in namespace:
                namespace[setter_name] = make_setter(attr)

        # Створюємо фінальний клас
        return super().__new__(mcs, name, bases, namespace)


# ------------------------- Приклад використання -------------------------

class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


# Створення об'єкта
p = Person()

# Використання автоматично створених методів
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())   # 31
