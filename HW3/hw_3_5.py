class MyList:
    """
    Custom class that mimics some built-in list behaviors.
    Implements special methods for len(), sum(), and min().
    """

    def __init__(self, data):
        """
        Initialize with a list of numbers.

        Args:
            data (list): A list of numeric values.

        Raises:
            TypeError: If data is not a list.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be provided as a list")
        self.data = data

    def __len__(self):
        """
        Return number of elements (for len()).

        Returns:
            int: The number of elements in the list.
        """
        count = 0
        for _ in self.data:  # manually count elements
            count += 1
        return count

    def __iter__(self):
        """
        Allow iteration over elements (needed for sum and min).

        Returns:
            iterator: An iterator over the list's data.
        """
        return iter(self.data)

    def __getitem__(self, index):
        """
        Get element by index like regular list[index].

        Args:
            index (int): The index of the element.

        Returns:
            element: The value at the specified index.
        """
        return self.data[index]

    def __repr__(self):
        """
        String representation for easy debugging and display.

        Returns:
            str: A string representation of the object.
        """
        return f"MyList({self.data})"


# Testing

# Створюємо свій список
numbers = MyList([5, 3, 8, 2, 7])
print("My custom list:", numbers)

# Перевірка len()
print("len(numbers) =", len(numbers))  # 5

# Перевірка sum()
total = 0
for num in numbers:
    total += num
print("sum(numbers) =", total)  # 25

# Перевірка min()
min_value = None
for num in numbers:
    if min_value is None or num < min_value:
        min_value = num
print("min(numbers) =", min_value)  # 2

# Перевірка доступу по індексу
print("numbers[2] =", numbers[2])  # 8

# Перевірка ітерації в циклі for
print("\nIterating over numbers:")
for num in numbers:
    print(num)
