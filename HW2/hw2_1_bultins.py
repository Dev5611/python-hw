import builtins
from typing import Any


def my_sum(*args: Any, **kwargs: Any) -> None:
    """
    Custom function that demonstrates overriding a built-in function name.
    Instead of summing, it simply prints a message.
    """
    print("This is my custom sum function!")


# Create a list of numbers
numbers: list[int] = [1, 2, 3, 4, 5]

# Call the built-in sum function to add up the numbers
print("Calling the built-in sum:", builtins.sum(numbers))

# Call our custom my_sum function
my_sum(numbers)

# Call the built-in sum again
print("Calling the built-in sum again:", builtins.sum(numbers))
