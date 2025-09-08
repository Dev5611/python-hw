class Person:
    """
    Class to represent a person with name and age.

    Supports comparison by age:
    - lt  (less than)
    - eq  (equal)
    - gt  (greater than)
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """Check if this person is younger than another."""
        return self.age < other.age

    def __eq__(self, other: "Person") -> bool:
        """Check if this person has the same age as another."""
        return self.age == other.age

    def __gt__(self, other: "Person") -> bool:
        """Check if this person is older than another."""
        return self.age > other.age

    def __repr__(self) -> str:
        """String representation for easy printing."""
        return f"Person(name='{self.name}', age={self.age})"


# Example usage

# Створюємо список людей
people = [
    Person("Олег", 25),
    Person("Аліна", 19),
    Person("Максим", 30),
    Person("Ірина", 22),
]

print("Початковий список:")
print(people)  # показує у форматі Person(name='...', age=...)

# Сортування за віком (використовує lt)
sorted_people = sorted(people)
print("\nВідсортований список за віком:")
print(sorted_people)

# Порівняння окремих об'єктів
print("\nПриклади порівнянь:")
print(people[0] < people[2])  # True, якщо Олег молодший за Максима
print(people[0] == people[2])  # False, якщо вік різний
print(people[0] > people[1])  # True, якщо Олег старший за Аліну
