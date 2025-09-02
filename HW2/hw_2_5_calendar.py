def calendar():
    """
    Closure that provides functions for:
    - adding events
    - removing events
    - viewing events
    Events are stored in an enclosing scope variable (not global).
    Demonstrates the use of 'nonlocal'.
    """
    events: list[str] = []  # Enclosing scope

    def add_event(event: str) -> None:
        """Add event to the enclosing list using nonlocal."""
        nonlocal events
        events.append(event)
        print(f"Подію «{event}» додано")

    def remove_event(event: str) -> None:
        """Remove event from the enclosing list using nonlocal."""
        nonlocal events
        if event in events:
            events.remove(event)
            print(f"Подію «{event}» видалено")
        else:
            print(f"Подію «{event}» не знайдено")

    def view_events() -> None:
        """View all upcoming events."""
        if not events:
            print("Майбутніх подій не знайдено")
        else:
            print("Майбутні події:")
            for e in events:
                print(f" • {e}")

    return add_event, remove_event, view_events


# Example usage
add_event, remove_event, view_events = calendar()

add_event("Воркшоп 20.09.25")
add_event("Тестування 24.09.25")
view_events()

remove_event("Тестування 24.09.25")
view_events()
