from __future__ import annotations

from typing import Any, Callable, Dict


class GameEventException(Exception):
    """
    Custom exception to signal an in-game event that occurred.

    Attributes:
        event_type (str): Type of the event (e.g., "death", "levelUp").
        details (dict[str, Any]): Extra structured info about the event
            (e.g., reason, killer, location; new_level, gained_xp).
    """

    def __init__(self, event_type: str, details: Dict[str, Any]) -> None:
        self.event_type = event_type
        self.details = details
        super().__init__(f"Game event occurred: {event_type}")

    def __repr__(self) -> str:
        return f"GameEventException(event_type={self.event_type!r}, details={self.details!r})"


# ------------------------- Event raising API -------------------------

def complete_event(event_type: str, **details: Any) -> None:
    """
    Simulate the end of a game event and raise GameEventException with details.

    Example:
        complete_event("death", reason="sword hit", killer="Goblin", location="Dungeon")
        complete_event("levelUp", new_level=5, gained_xp=300)
    """
    raise GameEventException(event_type=event_type, details=details)


# ------------------------- Handlers & dispatcher -------------------------

EventHandler = Callable[[GameEventException], None]


def handle_death(event: GameEventException) -> None:
    """Handle a death event: show reason, killer, location, etc."""
    reason = event.details.get("reason", "unknown")
    killer = event.details.get("killer", "unknown")
    location = event.details.get("location", "unknown")
    print(f"[UI] You died. Reason: {reason}. Killer: {killer}. Location: {location}.")
    print("[SAVE] Death event logged.")


def handle_level_up(event: GameEventException) -> None:
    """Handle a level up event: show new level and XP gained."""
    new_level = event.details.get("new_level")
    gained_xp = event.details.get("gained_xp")
    print(f"[UI] Level up! New level: {new_level}, XP gained: {gained_xp}.")
    print("[SAVE] Level-up event logged.")


def handle_generic(event: GameEventException) -> None:
    """Fallback handler for any other event types."""
    print(f"[UI] Event: {event.event_type} | Details: {event.details}")
    print("[SAVE] Generic event logged.")


# Map each known event type to a specific handler (easily extensible).
EVENT_HANDLERS: Dict[str, EventHandler] = {
    "death": handle_death,
    "levelUp": handle_level_up,
}


def dispatch_event_exception(event_exc: GameEventException) -> None:
    """
    Route the exception to a specific handler based on event_type.
    Falls back to a generic handler if event_type is unknown.
    """
    handler = EVENT_HANDLERS.get(event_exc.event_type, handle_generic)
    handler(event_exc)


# ------------------------- Demo: raising & handling -------------------------

print("=== Game loop demo: raising and handling GameEventException ===")

# 1) "death" event
try:
    # ... gameplay ...
    complete_event("death", reason="sword hit", killer="Goblin", location="Dungeon")
except GameEventException as e:
    dispatch_event_exception(e)
finally:
    print("[FINALLY] Resources cleaned up for death event.\n")

# 2) "levelUp" event
try:
    # ... gameplay ...
    complete_event("levelUp", new_level=5, gained_xp=300)
except GameEventException as e:
    dispatch_event_exception(e)
finally:
    print("[FINALLY] Resources cleaned up for levelUp event.\n")

# 3) Unknown/other event type (shows generic handling)
try:
    # ... gameplay ...
    complete_event("questCompleted", quest_id=42, rewards=["gold", "sword"])
except GameEventException as e:
    dispatch_event_exception(e)
finally:
    print("[FINALLY] Resources cleaned up for generic event.\n")
