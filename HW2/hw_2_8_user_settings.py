from typing import Any, Callable, Tuple


def create_user_settings() -> Tuple[
    Callable[[str, Any], None],
    Callable[[str], Any],
    Callable[[], None],
]:
    """
    Demonstrates LEGB principle and the use of nonlocal via a closure.

    (Local): variables inside set_setting/get_setting/view_settings
    (Enclosing): 'settings' defined in create_user_settings
    (Global): the function create_user_settings itself, imported modules
    (Built-in): functions like print(), dict, str

    Returns:
        Tuple containing three functions:
            - set_setting(key: str, value: Any) -> None
            - get_setting(key: str) -> Any
            - view_settings() -> None
    """
    # Enclosing scope variable
    settings: dict[str, Any] = {
        "theme": "light",
        "language": "en",
        "notifications": True,
    }

    def set_setting(key: str, value: Any) -> None:
        """
        L = Local: key, value
        E = settings (nonlocal)
        """
        nonlocal settings
        settings[key] = value
        print(f"Налаштування «{key}» збережено: {value}")

    def get_setting(key: str) -> Any:
        """
        L = Local: key
        E = settings
        """
        return settings.get(key, f"Налаштування «{key}» не знайдено")

    def view_settings() -> None:
        """
        L = Local: k, v (loop vars)
        E = settings
        """
        print("Поточні налаштування користувача:")
        for k, v in settings.items():
            print(f" • {k}: {v}")

    return set_setting, get_setting, view_settings


# Example usage
set_setting, get_setting, view_settings = create_user_settings()

# Global: direct call to a closure
view_settings()  # show defaults

set_setting("theme", "dark")
set_setting("language", "uk")
set_setting("notifications", False)

view_settings()  # show updated
print("Мова інтерфейсу:", get_setting("language"))
