import importlib
import inspect


def analyze_module(module_name: str) -> None:
    """
    Analyze a Python module by its name and display:
      - All functions with their signatures.
      - All classes defined in the module.

    Args:
        module_name (str): The name of the module to analyze.

    Raises:
        ModuleNotFoundError: If the specified module cannot be imported.
    """
    try:
        # Динамічно імпортуємо модуль
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
        return

    print(f"\nАналіз модуля: {module_name}\n")

    # --- Функції ---
    functions = inspect.getmembers(module, inspect.isfunction)
    print("Функції:")
    if not functions:
        print(" - <немає функцій>")
    else:
        for func_name, func_obj in functions:
            signature = str(inspect.signature(func_obj))
            print(f" - {func_name}{signature}")

    print()

    # --- Класи ---
    classes = inspect.getmembers(module, inspect.isclass)
    print("Класи:")
    if not classes:
        print(" - <немає класів>")
    else:
        for class_name, _ in classes:
            print(f" - {class_name}")

    print()


# ------------------------- Приклад використання -------------------------

# Аналізуємо стандартний модуль math
analyze_module("math")
