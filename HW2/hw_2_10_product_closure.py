from typing import Callable, Tuple


def create_product(name: str, price: float, quantity: int) -> Tuple[
    Callable[[float], None], Callable[[], None]
]:
    """
    Create a product with name, price and quantity.
    Returns two functions: update_price and view_product.
    Demonstrates closures and use of 'nonlocal'.
    """
    current_price = price  # Enclosing scope

    def update_price(new_price: float) -> None:
        """
        Update the product price.
        Uses 'nonlocal' to modify enclosing variable.
        """
        nonlocal current_price
        current_price = new_price
        print(f"Ціну товару «{name}» змінено на {current_price:.2f}")

    def view_product() -> None:
        """Print current product info."""
        print(
            f"Товар: {name}, "
            f"ціна: {current_price:.2f}, "
            f"кількість: {quantity}"
        )

    return update_price, view_product


# --- Example usage ---
update_price, view_product = create_product("Ноутбук", 25000.0, 5)

view_product()        # shows initial product
update_price(23000.0) # updates price
view_product()        # shows updated product