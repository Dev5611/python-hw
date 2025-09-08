## README.md

# Python Homework Project

## Description

This repository contains multiple Python homework assignments organized into separate folders:

* **HW1** – Basics of Python: calculations, classes, and fundamental operations.
* **HW2** – Functions, scopes (LEGB rule), closures, and decorators.
* **HW3** – Dunder methods, custom class behaviors, properties, and descriptors.

Each homework folder contains individual scripts for each task.
The code includes:

* **Type annotations** for clarity.
* **Docstrings** for documentation.
* Formatting that follows **PEP 8** style guidelines.

---

## Repository Structure

```
Python-HW-Project/
├── HW1/                # Homework 1: Python basics
│   ├── HW1_1.py        # Circle area calculation
│   ├── HW1_2.py        # Rectangle class
│   └── README.md       # Detailed HW1 documentation
│
├── HW2/                # Homework 2: Functions and scopes
│   ├── hw2_1.py        # Built-in function override (sum)
│   ├── hw2_2.py        # Subscription manager
│   ├── hw2_3.py        # Discount system with global/nonlocal
│   ├── hw2_4.py        # Training timer simulation
│   ├── hw2_5.py        # Calendar using closures
│   ├── hw2_6.py        # Calculator using closures
│   ├── hw2_7.py        # Expense tracker
│   ├── hw2_8.py        # User settings with closures
│   ├── hw2_9.py        # Memoization example (Fibonacci)
│   └── hw2_10.py       # Product creation with closures
│
├── HW3/                # Homework 3: Advanced OOP concepts
│   ├── hw_3_1.py       # Fraction class
│   ├── hw_3_2.py       # Vector class (basic operations)
│   ├── hw_3_3.py       # Person class comparison
│   ├── hw_3_4.py       # Binary number operations
│   ├── hw_3_5.py       # Custom built-in function implementations
│   ├── hw_3_6.py       # User class with @property
│   ├── hw_3_7.py       # Vector class with comparisons
│   ├── hw_3_8.py       # Price class
│   └── hw_3_9.py       # Comparing getter/setter, @property, and descriptors
│
└── README.md           # Global README for entire project
```

---

## Homework Overviews

### **HW1 – Python Basics**

Focus on fundamental Python concepts and object-oriented programming basics.

**Topics:**

* Calculations with user input.
* Creating classes and methods.
* Type annotations and PEP 8 formatting.

**Tasks:**

1. **HW1\_1.py** – Calculate the area of a circle from user input.
2. **HW1\_2.py** – Rectangle class with:

   * Area
   * Perimeter
   * Square check
   * Resize functionality

---

### **HW2 – Functions, Scopes, Closures, Decorators**

Explore the **LEGB rule** (Local, Enclosing, Global, Built-in), closures, and decorators.

**Key concepts:**

* Global and local variables.
* `global` and `nonlocal` keywords.
* Functions returning functions.
* Basic decorator usage.

**Example tasks:**

* Override a built-in function (`sum`).
* Subscription manager using nested functions.
* Calendar app with closures.
* Memoization for Fibonacci numbers.
* Simple calculator built with closures.

---

### **HW3 – Advanced OOP**

Advanced object-oriented programming with Python-specific features.

**Topics:**

* Dunder methods (`__add__`, `__eq__`, `__repr__`, etc.).
* Implementing custom behaviors for built-in functions.
* Using `@property` for controlled attribute access.
* Descriptors for advanced attribute management.
* Financial calculations and currency conversions.

**Example tasks:**

* Fraction class supporting arithmetic.
* Vector class with arithmetic and comparisons.
* Price class with accurate rounding using `Decimal`.
* Product class showing three approaches to managing attributes:

  * Classic getter/setter
  * `@property`
  * Custom descriptors with currency conversion.

---

## How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project folder:

   ```bash
   cd Python-HW-Project
   ```

3. Run a specific homework task:

   ```bash
   python HW2/hw2_3.py
   ```

   or

   ```bash
   python HW3/hw_3_8.py
   ```

---

## Requirements

* Python **3.8** or higher
* No external libraries required — only Python's **standard library** is used:

  * `math` for calculations.
  * `decimal` for financial rounding.
  * `re` for email validation.

---

## Notes and Enhancements

Some tasks include additional improvements beyond the basic requirements:

* **Financial rounding** with `Decimal` and `ROUND_HALF_UP` for accurate money handling.
* **Descriptors for automatic currency conversion** in HW3.
* **Extra tests** to verify code behavior and validation.
* Enhanced structure for scalability and maintainability.

---

## License

This repository is for educational purposes only.
All code examples are free to use and modify.
