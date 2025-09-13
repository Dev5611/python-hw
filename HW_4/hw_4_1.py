from decimal import Decimal, InvalidOperation, Overflow, getcontext
import sys
import re


class UnknownOperationError(Exception):
    """Custom exception for unsupported operations."""
    pass


# ---- Decimal context (precision & overflow limits) ----
ctx = getcontext()
ctx.prec = 28      # significant digits
ctx.Emax = 999999  # overflow upper exponent bound
ctx.Emin = -999999 # overflow lower exponent bound


def calculate(a: Decimal, b: Decimal, operation: str) -> Decimal:
    """
    Perform basic arithmetic operations with Decimal.

    Args:
        a (Decimal): First number.
        b (Decimal): Second number.
        operation (str): One of '+', '-', '*', '/'.

    Raises:
        ZeroDivisionError: On division by zero.
        UnknownOperationError: If operation is unsupported.
    """
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    raise UnknownOperationError(f"Unknown operation: '{operation}'")


# Regex для парсингу "число op число" з/без пробілів, підтримує десяткові та знак
EXPR = re.compile(r"""
    ^\s*
    ([+-]?\d+(?:\.\d+)?)
    \s*([+\-*/])\s*
    ([+-]?\d+(?:\.\d+)?)
    \s*$
""", re.VERBOSE)

print("Simple Console Calculator")
print("Supported operations: +, -, *, /")
print("Type 'exit' to quit.")
print("Examples: 23+2,  3.5 *2,  -10/  4")

while True:
    try:
        user_input = input("\nEnter expression: ").strip()
        if user_input.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        m = EXPR.match(user_input)
        if not m:
            raise ValueError("Input must be in format: number[.number] op number[.number]")

        left_str, op, right_str = m.groups()

        # Convert to Decimal for accurate decimal arithmetic
        left = Decimal(left_str)
        right = Decimal(right_str)

        result = calculate(left, right, op)
        print(f"Result: {result}")

    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except InvalidOperation:
        print("Error: Invalid number format. Please enter valid decimal numbers.")
    except Overflow:
        print("Error: Number too large (overflow).")
    except ValueError as ve:
        print(f"Error: {ve}")
    except UnknownOperationError as uoe:
        print(f"Error: {uoe}")
    except KeyboardInterrupt:
        print("\nCalculator stopped by user.")
        sys.exit(0)
