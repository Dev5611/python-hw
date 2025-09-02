from typing import Callable


def safe_div(a: float, b: float) -> float:
    """
    Perform safe division.

    Args:
        a (float): Dividend.
        b (float): Divisor.

    Returns:
        float: Result of division.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе")
    return a / b


def create_calculator(operator: str) -> Callable[[float, float], float]:
    """
    Create a calculator function for the given operator.

    Args:
        operator (str): One of '+', '-', '*', '/'.

    Returns:
        Callable[[float, float], float]: A function that performs the operation.

    Raises:
        ValueError: If operator is not supported.
    """
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': safe_div,  # окрема функція для ділення
    }

    if operator not in operations:
        raise ValueError(f"Непідтримуваний оператор: {operator}")

    def calculate(a: float, b: float) -> float:
        return operations[operator](a, b)

    return calculate


# Example usage
add = create_calculator('+')
sub = create_calculator('-')
mul = create_calculator('*')
div = create_calculator('/')

print(add(10, 5))   # 15
print(sub(10, 5))   # 5
print(mul(10, 5))   # 50
print(div(10, 5))   # 2.0
