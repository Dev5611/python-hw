class InsufficientFundsException(Exception):
    """
    Custom exception raised when an account has insufficient funds
    to complete a transaction.

    Attributes:
        required_amount (float): Amount needed to complete the transaction.
        current_balance (float): Current balance in the account.
        currency (str): Currency code, e.g., 'USD', 'EUR'.
        transaction_type (str): Type of transaction, e.g., 'withdrawal', 'purchase'.
    """

    def __init__(
        self,
        required_amount: float,
        current_balance: float,
        currency: str = "USD",
        transaction_type: str = "transaction",
    ) -> None:
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
        super().__init__(self._generate_message())

    def _generate_message(self) -> str:
        """Create a descriptive message about insufficient funds."""
        return (
            f"Insufficient funds for {self.transaction_type}. "
            f"Required: {self.required_amount:.2f} {self.currency}, "
            f"Available: {self.current_balance:.2f} {self.currency}."
        )

    def __repr__(self) -> str:
        return (
            f"InsufficientFundsException("
            f"required_amount={self.required_amount}, "
            f"current_balance={self.current_balance}, "
            f"currency='{self.currency}', "
            f"transaction_type='{self.transaction_type}')"
        )


# ------------------------- Bank Account Class -------------------------

class BankAccount:
    """Simple bank account simulation."""

    def __init__(self, balance: float, currency: str = "USD") -> None:
        self.balance = balance
        self.currency = currency

    def withdraw(self, amount: float) -> None:
        """
        Attempt to withdraw money from the account.

        Raises:
            InsufficientFundsException: if balance is less than amount.
        """
        if amount > self.balance:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="withdrawal",
            )

        self.balance -= amount
        print(f"[OK] Withdrawal successful! Remaining balance: {self.balance:.2f} {self.currency}")

    def purchase(self, amount: float) -> None:
        """
        Attempt to make a purchase.

        Raises:
            InsufficientFundsException: if balance is less than amount.
        """
        if amount > self.balance:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="purchase",
            )

        self.balance -= amount
        print(f"[OK] Purchase successful! Remaining balance: {self.balance:.2f} {self.currency}")


# ------------------------- Usage Example -------------------------

account = BankAccount(balance=100.00, currency="USD")

try:
    print("Attempting withdrawal of $120.00...")
    account.withdraw(120.00)  # недостатньо коштів
except InsufficientFundsException as e:
    print(f"[ERROR] {e}")
finally:
    print("[FINALLY] Withdrawal process finished.\n")

try:
    print("Attempting purchase of $50.00...")
    account.purchase(50.00)  # достатньо коштів
except InsufficientFundsException as e:
    print(f"[ERROR] {e}")
finally:
    print("[FINALLY] Purchase process finished.\n")

try:
    print("Attempting another purchase of $70.00...")
    account.purchase(70.00)  # недостатньо коштів
except InsufficientFundsException as e:
    print(f"[ERROR] {e}")
finally:
    print("[FINALLY] Second purchase process finished.\n")
