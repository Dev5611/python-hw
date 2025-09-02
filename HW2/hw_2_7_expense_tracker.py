# Global variable to store total expenses
total_expense: float = 0.0


def add_expense(amount: float) -> None:
    """
    Add an expense to the global total_expense.
    Demonstrates use of the 'global' keyword.
    """
    global total_expense
    total_expense += amount
    print(f"Додано витрату: {amount:.2f}. Поточна сума: {total_expense:.2f}")


def get_expense() -> float:
    """
    Return the current total expenses.
    """
    return total_expense


# Simple console interface (no main function)
print("Трекер витрат")
print("Введіть число для додавання витрат або 'exit' для виходу")

while True:
    user_input = input("Введіть витрату: ")

    if user_input.lower() == "exit":
        print(f"Загальна сума витрат: {get_expense():.2f}")
        print("Програма завершена.")
        break

    try:
        amount = float(user_input)
        add_expense(amount)
    except ValueError:
        print("Помилка: введіть число або 'exit'")