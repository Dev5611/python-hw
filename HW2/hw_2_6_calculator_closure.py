def create_calculator(operator: str):
    """
    Create a calculator function for a given operator using a dictionary.
    Demonstrates closures: the returned function remembers the operator.

    Args:
        operator (str): One of '+', '-', '*', '/'.

    Returns:
        function: A function that takes two numbers and applies the operator.
    """

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Ділення на нуль неможливе"))
    }

    if operator not in operations:
        raise ValueError(f"Непідтримуваний оператор: {operator}")

    def calculate(a: float, b: float) -> float:
        """Perform calculation using the chosen operator from operations dict."""
        return operations[operator](a, b)

    return calculate


# --- Example usage ---
add = create_calculator('+')
sub = create_calculator('-')
mul = create_calculator('*')
div = create_calculator('/')

print(add(10, 5))   # 15
print(sub(10, 5))   # 5
print(mul(10, 5))   # 50
print(div(10, 5))   # 2.0
