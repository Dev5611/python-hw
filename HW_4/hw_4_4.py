class InsufficientResourcesException(Exception):
    """
    Custom exception for situations where the player does not have
    enough resources to perform an action.

    Attributes:
        required_resource (str): Name of the resource (e.g., 'gold', 'mana').
        required_amount (int | float): Amount of resource needed to perform the action.
        current_amount (int | float): Player's current resource amount.
    """

    def __init__(self, required_resource: str, required_amount: float, current_amount: float) -> None:
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        super().__init__(self._generate_message())

    def _generate_message(self) -> str:
        """Generate a descriptive error message."""
        return (
            f"Not enough {self.required_resource}! "
            f"Required: {self.required_amount}, "
            f"Available: {self.current_amount}."
        )

    def __repr__(self) -> str:
        return (
            f"InsufficientResourcesException("
            f"resource={self.required_resource!r}, "
            f"required={self.required_amount}, "
            f"current={self.current_amount})"
        )


# ------------------------- Example game logic -------------------------

class Player:
    """Simple player class with resources like gold and mana."""

    def __init__(self, gold: int, mana: int) -> None:
        self.gold = gold
        self.mana = mana

    def spend_resource(self, resource: str, amount: int) -> None:
        """
        Attempt to spend a resource. If insufficient, raise custom exception.

        Args:
            resource (str): Resource name, e.g., 'gold' or 'mana'.
            amount (int): How much to spend.
        """
        current_amount = getattr(self, resource, None)
        if current_amount is None:
            raise ValueError(f"Unknown resource: {resource}")

        if current_amount < amount:
            raise InsufficientResourcesException(resource, amount, current_amount)

        setattr(self, resource, current_amount - amount)
        print(f"[OK] {amount} {resource} spent successfully. Remaining: {current_amount - amount}")


# ------------------------- Usage demo -------------------------

player = Player(gold=50, mana=20)

try:
    print("Attempting to buy a sword for 70 gold...")
    player.spend_resource("gold", 70)  # недостатньо золота
except InsufficientResourcesException as e:
    print(f"[ERROR] {e}")
finally:
    print("[FINALLY] Resource check completed.\n")

try:
    print("Casting a spell that costs 10 mana...")
    player.spend_resource("mana", 10)  # вистачає мани
except InsufficientResourcesException as e:
    print(f"[ERROR] {e}")
finally:
    print("[FINALLY] Resource check completed.\n")

try:
    print("Casting a powerful spell that costs 15 mana...")
    player.spend_resource("mana", 15)  # недостатньо мани
except InsufficientResourcesException as e:
    print(f"[ERROR] {e}")
finally:
    print("[FINALLY] Resource check completed.\n")
