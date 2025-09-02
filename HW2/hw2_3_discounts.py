# Task 3: Store order system with discounts

# Global discount (10%)
discount: float = 0.10


def create_order(price: float) -> None:
    """
    Create an order and calculate prices with discounts.
    Demonstrates global, local, and nonlocal scopes.

    Args:
        price (float): The initial price of the product. Must be non-negative.

    Raises:
        ValueError: If the price is negative.
    """
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною.")

    # Local variable: final price with the base/global discount
    final_price: float = price * (1 - discount)

    def apply_vip_discount() -> None:
        """
        Apply an additional VIP discount (5%) to the final price.
        Uses 'nonlocal' to modify final_price in enclosing scope.
        """
        nonlocal final_price
        vip_discount: float = 0.05
        final_price = final_price * (1 - vip_discount)

    # Save the price with only the global discount
    regular_price: float = final_price

    # Apply VIP discount (modifies final_price using nonlocal)
    apply_vip_discount()
    vip_price: float = final_price

    # Print results
    print(f"Початкова ціна: {price:.2f}")
    print(f"Ціна зі знижкою {int(discount * 100)}%: {regular_price:.2f}")
    print(
        f"Ціна зі знижкою {int(discount * 100)}% + "
        f"додатково 5% для VIP: {vip_price:.2f}"
    )


# --- Example usage ---
create_order(1000.0)   # OK
# create_order(-500.0)  # Raises ValueError
