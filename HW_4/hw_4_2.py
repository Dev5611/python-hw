import sys


def calculate_average_from_file(filename: str) -> float:
    """
    Reads numbers from a file and calculates their average.

    Args:
        filename (str): Path to the text file.

    Returns:
        float: The average of numbers in the file.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If file contains invalid (non-numeric) data or is empty.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # Перевірка на порожній файл
            if not lines:
                raise ValueError("File is empty. Cannot calculate average.")

            # Перетворюємо рядки в числа, ігноруючи зайві пробіли
            numbers = []
            for line in lines:
                stripped_line = line.strip()
                if not stripped_line:  # Пропускаємо порожні рядки
                    continue
                try:
                    number = float(stripped_line)
                    numbers.append(number)
                except ValueError:
                    raise ValueError(f"Invalid data found in file: '{stripped_line}'")

            # Перевірка, чи є хоча б два числа
            if len(numbers) == 0:
                raise ValueError("No valid numbers found in the file.")
            if len(numbers) == 1:
                print("Warning: Only one number in file. Average equals this number.")

            return sum(numbers) / len(numbers)

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' was not found.")


# --- Виконання ---
filename = input("Enter file name: ").strip()

try:
    average = calculate_average_from_file(filename)
    print(f"Average of numbers in '{filename}': {average}")
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except ValueError as val_error:
    print(f"Error: {val_error}")
except Exception as e:
    print(f"Unexpected error: {e}")
