from typing import List

# Global variable that stores the list of subscribers
subscribers: List[str] = []


def subscribe(name: str) -> str:
    """
    Add a subscriber to the global subscribers list.

    Inside this function, a nested function confirm_subscription()
    is defined, which returns a confirmation message for the given subscriber.

    Args:
        name (str): The name of the subscriber.

    Returns:
        str: Confirmation message.
    """
    if not name.strip():
        return "Ім’я підписника не може бути порожнім."

    subscribers.append(name)

    def confirm_subscription() -> str:
        """
        Nested function that confirms the subscription
        using the subscriber's name.
        """
        return f"Підписка підтверджена для {name}"

    return confirm_subscription()


def unsubscribe(name: str) -> str:
    """
    Remove a subscriber from the global subscribers list if present.

    Args:
        name (str): The name of the subscriber to remove.

    Returns:
        str: Result message.
    """
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} успішно відписаний"
    return f"{name} не знайдено у списку підписників"


# Example usage
print(subscribe("Олена"))   # Підписка підтверджена для Олена
print(subscribe("Ігор"))    # Підписка підтверджена для Ігор
print(subscribers)          # ['Олена', 'Ігор']

print(unsubscribe("Ігор"))  # Ігор успішно відписаний
print(subscribers)          # ['Олена']
