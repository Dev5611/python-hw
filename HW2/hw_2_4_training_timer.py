# Task 4: Training session timer

# Global scope variable lives in the module namespace
default_time: int = 60


def training_session(rounds: int) -> None:
    """
    Simulate a training session with multiple rounds.

    Demonstrates LEGB principle, namespace, and usage of 'nonlocal'.

    Args:
        rounds (int): Number of training rounds. Must be >= 1.

    Raises:
        ValueError: If the number of rounds is less than 1.
    """
    if rounds < 1:
        raise ValueError("Кількість раундів має бути не менше 1.")

    # Local scope variable belongs to training_session
    time_per_round: int = default_time

    # Enclosing scope nested function can see and modify time_per_round
    def adjust_time(adjustment: int) -> None:
        """
        Adjust the training time for the current round.

        Uses 'nonlocal' to modify the variable from enclosing scope.
        """
        nonlocal time_per_round
        time_per_round -= adjustment

    # Built-in scope functions like print(), range() are always available
    for round_num in range(1, rounds + 1):
        if round_num > 1:
            adjust_time(5)  # decrease 5 minutes per round after the first
            print(f"Раунд {round_num}: {time_per_round} хвилин (після коригування часу)")
        else:
            print(f"Раунд {round_num}: {time_per_round} хвилин")


# --- Example usage ---
training_session(3)