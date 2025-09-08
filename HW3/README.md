## README.md

# Python HW3: Dunder Methods, Properties, and Descriptors

## Description

This repository contains solutions for the third Python homework, focusing on:

* **Dunder methods** (`__init__`, `__add__`, `__eq__`, etc.)
* **Properties with `@property` decorator**
* **Descriptors** for advanced attribute management
* Implementation of custom behaviors for built-in functions
* Currency conversion and financial data handling

Each task demonstrates a specific Python concept and includes type annotations, docstrings, and code that follows PEP 8 guidelines.

---

## Table of Contents

1. [Task 1: Fraction Class](#task-1-fraction-class)
2. [Task 2: Vector Class (Basic Operations)](#task-2-vector-class-basic-operations)
3. [Task 3: Person Class Comparison](#task-3-person-class-comparison)
4. [Task 4: Binary Number Operations](#task-4-binary-number-operations)
5. [Task 5: Custom Built-in Function Implementations](#task-5-custom-built-in-function-implementations)
6. [Task 6: User Class with Properties](#task-6-user-class-with-properties)
7. [Task 7: Vector Class with Comparisons](#task-7-vector-class-with-comparisons)
8. [Task 8: Price Class](#task-8-price-class)
9. [Task 9: Comparing Getter/Setter, `@property`, and Descriptors](#task-9-comparing-gettersetter-property-and-descriptors)

---

## Task 1: Fraction Class

**Goal:**
Create a class that represents fractions and supports basic arithmetic operations.

**Features:**

* Supports addition, subtraction, multiplication, and division via dunder methods:

  * `__add__`, `__sub__`, `__mul__`, `__truediv__`
* Proper string representation using `__repr__` in format `"numerator/denominator"`

**Example:**

```python
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)  # 5/6
```

---

## Task 2: Vector Class (Basic Operations)

**Goal:**
Implement a vector class for basic arithmetic operations.

**Features:**

* Addition (`__add__`) and subtraction (`__sub__`)
* Scalar multiplication (`__mul__`)
* Dot product
* Method to calculate vector length

**Example:**

```python
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)  # Vector([5, 7, 9])
print(v1 * v2)  # 32
```

---

## Task 3: Person Class Comparison

**Goal:**
Create a class `Person` that supports comparison by age.

**Features:**

* Dunder methods for comparison:

  * `__lt__` (less than)
  * `__eq__` (equal to)
  * `__gt__` (greater than)
* Sorting a list of `Person` objects by age.

**Example:**

```python
people = [Person("Alice", 30), Person("Bob", 25)]
people.sort()
```

---

## Task 4: Binary Number Operations

**Goal:**
Implement binary operations for custom `BinaryNumber` class.

**Features:**

* `__and__` (AND)
* `__or__` (OR)
* `__xor__` (XOR)
* `__invert__` (NOT)

**Example:**

```python
a = BinaryNumber(0b1010)
b = BinaryNumber(0b1100)
print(a & b)  # 8
```

---

## Task 5: Custom Built-in Function Implementations

**Goal:**
Implement custom versions of `len()`, `sum()`, and `min()` functions using dunder methods.

**Features:**

* `__len__` for length calculation
* `__iter__` and `__getitem__` for iteration
* Custom `sum` and `min` functions that work on custom objects.

---

## Task 6: User Class with Properties

**Goal:**
Create a `User` class with attributes:

* `first_name`
* `last_name`
* `email`

**Features:**

* Access attributes using `@property` and setters.
* Validate email format using regular expressions.

---

## Task 7: Vector Class with Comparisons

**Goal:**
Extend the vector class to include comparison by vector length.

**Features:**

* Compare vectors using `__lt__`, `__eq__`, `__gt__`.

---

## Task 8: Price Class

**Goal:**
Create a `Price` class that represents a product price and supports rounding to two decimals.

**Features:**

* Addition and subtraction using `__add__` and `__sub__`
* Comparisons (`__eq__`, `__lt__`, `__gt__`)
* Alternative constructor `from_cents()`
* **Improvement:** Added financial rounding using `Decimal` and `ROUND_HALF_UP` for accurate monetary calculations.

---

## Task 9: Comparing Getter/Setter, `@property`, and Descriptors

**Goal:**
Demonstrate three different approaches to manage the `price` attribute in a `Product` class:

1. **Classic getter and setter methods** (`get_price`, `set_price`)
2. **Using `@property` decorator**
3. **Using custom descriptors**

**Additional improvements:**

* Added `CurrencyDescriptor` for validating and managing currency codes (`USD`, `EUR`).
* Added `PriceDescriptor` to store base prices in USD and automatically convert to/from the current currency.
* Implemented financial rounding with `Decimal`.
* Centralized validation to prevent negative prices.

**Example:**

```python
product = ProductWithDescriptor("Headset", price=100.0, currency="USD")
print(product)  # ProductWithDescriptor(name='Headset', price=100.00 USD)

product.currency = "EUR"
print(product)  # Converted automatically to EUR
```

---

## Notes and Enhancements

Some improvements were added beyond the base requirements:

* **Financial rounding** using `Decimal` for accuracy.
* **Automatic currency conversion** with descriptors.
* **Validation logic** centralized for all approaches.
* Proper ordering of class definitions to prevent `NameError`.
* Added extra tests for all three approaches to ensure correctness.

---

## Requirements

* Python 3.8 or higher
* Standard library only (`decimal`, `re` used for email validation).

---

## How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:

   ```bash
   cd HW3
   ```
3. Run any individual script:

   ```bash
   python hw_3_1.py
   ```

---

## General Structure

```
HW3/
├── hw_3_1.py   # Fraction class
├── hw_3_2.py   # Vector class basic operations
├── hw_3_3.py   # Person class comparison
├── hw_3_4.py   # Binary operations
├── hw_3_5.py   # Custom built-in functions
├── hw_3_6.py   # User class with @property
├── hw_3_7.py   # Vector class with comparisons
├── hw_3_8.py   # Price class
└── hw_3_9.py   # Comparing approaches for price management
```

---

## License

This project is for educational purposes only.
No external libraries are required.
