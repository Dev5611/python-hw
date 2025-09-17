class MutableClass:
    """
    Клас, який дозволяє динамічно додавати та видаляти атрибути під час виконання.

    Методи:
        add_attribute(name, value): додає атрибут з заданим ім'ям та значенням.
        remove_attribute(name): видаляє атрибут за його ім'ям.
    """

    def add_attribute(self, name: str, value) -> None:
        """
        Додає атрибут об'єкту динамічно.

        Args:
            name (str): Ім'я атрибуту.
            value: Значення, яке буде призначене атрибуту.
        """
        setattr(self, name, value)
        print(f"[INFO] Атрибут '{name}' додано зі значенням: {value}")

    def remove_attribute(self, name: str) -> None:
        """
        Видаляє атрибут об'єкту динамічно.

        Args:
            name (str): Ім'я атрибуту, який потрібно видалити.

        Raises:
            AttributeError: Якщо атрибут з таким ім'ям не існує.
        """
        if hasattr(self, name):
            delattr(self, name)
            print(f"[INFO] Атрибут '{name}' видалено")
        else:
            raise AttributeError(f"Атрибут '{name}' не знайдено, неможливо видалити")


# ------------------------- Приклад використання -------------------------

# Створення екземпляра класу
obj = MutableClass()

# Додаємо атрибут динамічно
obj.add_attribute("name", "Python")
print(obj.name)  # Python

# Видаляємо атрибут динамічно
obj.remove_attribute("name")

# Наступний рядок викличе помилку, бо атрибут вже видалено:
# print(obj.name)
