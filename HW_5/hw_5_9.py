class DynamicProperties:
    """
    Клас, що дозволяє динамічно додавати властивості (properties)
    з геттерами та сеттерами під час виконання програми.

    Методи:
        add_property(name, default_value):
            створює нову властивість з геттером і сеттером.
    """

    def add_property(self, name: str, default_value=None) -> None:
        """
        Додає динамічну властивість до класу за допомогою built-in функції property().

        Args:
            name (str): Назва нової властивості.
            default_value (Any): Початкове значення властивості (за замовчуванням None).
        """
        private_name = f"_{name}"  # приховане поле для збереження значення
        setattr(self, private_name, default_value)

        # --- Getter ---
        def getter(instance):
            return getattr(instance, private_name)

        # --- Setter ---
        def setter(instance, value):
            setattr(instance, private_name, value)

        # Створюємо property
        prop = property(getter, setter)

        # Додаємо до класу динамічно
        setattr(self.__class__, name, prop)


# ------------------------- Приклад використання -------------------------

# Створюємо екземпляр класу
obj = DynamicProperties()

# Додаємо динамічну властивість 'name' з дефолтним значенням
obj.add_property('name', 'default_name')

# Читаємо значення
print(obj.name)  # default_name

# Змінюємо значення
obj.name = "Python"
print(obj.name)  # Python

# Додаємо ще одну властивість
obj.add_property('version', 1.0)
print(obj.version)  # 1.0

# Змінюємо значення іншої властивості
obj.version = 3.12
print(obj.version)  # 3.12
