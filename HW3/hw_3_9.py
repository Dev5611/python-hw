from __future__ import annotations
from typing import Optional
from decimal import Decimal, ROUND_HALF_UP


# Функція для фінансового округлення (24.955 -> 24.96)
def round_money(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


# ============================================================
# 1) Клас із явними геттерами/сеттерами (get_price / set_price)
# ============================================================

class ProductWithGetSet:
    """
    Product with explicit getter/setter methods for `price`.
    Demonstrates the "classic" OOP style without @property.
    """

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self._price: float = 0.0
        self.set_price(price)  # validate on init

    def get_price(self) -> float:
        """Return current price."""
        return self._price

    def set_price(self, value: float) -> None:
        """
        Set price with validation (must be non-negative).

        Raises:
            ValueError: if value < 0
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round_money(value)

    def __repr__(self) -> str:
        return f"ProductWithGetSet(name='{self.name}', price={self._price:.2f})"


# ==========================================
# 2) Клас із властивістю через @property
# ==========================================

class ProductWithProperty:
    """
    Product using @property for controlled access to `price`.
    """

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self._price: float = 0.0
        self.price = price  # проходить через setter для валідації

    @property
    def price(self) -> float:
        """Get current price."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Set price with validation and rounding.

        Raises:
            ValueError: if value < 0
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round_money(value)

    def __repr__(self) -> str:
        return f"ProductWithProperty(name='{self.name}', price={self._price:.2f})"


# ============================================================
# 3) Дескриптори: валюта + ціна
# ============================================================

class CurrencyDescriptor:
    """
    Descriptor that stores and validates currency code.
    rates: USD per 1 unit of currency (демо-курси).
    """

    rates = {
        "USD": 1.0,   # 1 USD = 1.0 USD
        "EUR": 1.1,   # 1 EUR = 1.1 USD
    }

    def __set_name__(self, owner, name) -> None:
        self.name = name

    def __get__(self, instance, owner) -> Optional[str]:
        if instance is None:
            return self
        return instance.__dict__.get(self.name, "USD")

    def __set__(self, instance, value: str) -> None:
        if value not in self.rates:
            raise ValueError(f"Unsupported currency: {value}. Use one of {list(self.rates)}.")
        instance.__dict__[self.name] = value


class PriceDescriptor:
    """
    Descriptor that stores price internally in base USD,
    and converts on get/set according to the instance's currency.
    """

    def __set_name__(self, owner, name) -> None:
        self.name = name
        self._base_name = f"_{name}_usd_base"

    def __get__(self, instance, owner) -> float:
        if instance is None:
            return self
        base_usd = float(instance.__dict__.get(self._base_name, 0.0))
        currency = getattr(instance, "currency", "USD")
        usd_per_unit = CurrencyDescriptor.rates[currency]
        return round_money(base_usd / usd_per_unit)

    def __set__(self, instance, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        currency = getattr(instance, "currency", "USD")
        usd_per_unit = CurrencyDescriptor.rates[currency]
        instance.__dict__[self._base_name] = round_money(value * usd_per_unit)


class ProductWithDescriptor:
    """
    Product that uses descriptors for `price` and `currency`.
    Price is stored internally in USD, exposed in the chosen currency.
    """

    currency = CurrencyDescriptor()
    price = PriceDescriptor()

    def __init__(self, name: str, price: float, currency: str = "USD") -> None:
        self.name: str = name
        self.currency = currency
        self.price = price

    def __repr__(self) -> str:
        return f"ProductWithDescriptor(name='{self.name}', price={self.price:.2f} {self.currency})"


# ======================
# ТЕСТИ
# ======================

# 1) Явні геттери/сеттери ---
print("\n[1] ProductWithGetSet")
g = ProductWithGetSet("Mouse", 19.99)
print(g, "-> get_price():", g.get_price())
g.set_price(24.955)
print("Updated:", g, "-> get_price():", g.get_price())
try:
    g.set_price(-5)
except ValueError as e:
    print("Expected error (get/set):", e)

# 2) @property ---
print("\n[2] ProductWithProperty")
p = ProductWithProperty("Keyboard", 45.0)
print(p, "-> price:", p.price)
p.price = 49.999
print("Updated:", p, "-> price:", p.price)
try:
    p.price = -1
except ValueError as e:
    print("Expected error (@property):", e)

# 3) Дескриптори + валюта ---
print("\n[3] ProductWithDescriptor (+ currency)")
d = ProductWithDescriptor("Headset", price=100.0, currency="USD")
print(d)  # 100.00 USD

# Зміна валюти на EUR
d.currency = "EUR"
print("As EUR:", d)  # ~90.91 EUR (100 USD / 1.1)

# Встановлення нової ціни у EUR
d.price = 10.0       # 10 EUR -> 11.00 USD
print("Set 10.00 EUR ->", d)

# Перемикаємо назад у USD
d.currency = "USD"
print("As USD:", d)

# Перевірка помилки при від’ємній ціні
try:
    d.price = -3.0
except ValueError as e:
    print("Expected error (descriptor):", e)
