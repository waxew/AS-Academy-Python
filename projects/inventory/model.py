"""مدل دامنه پروژه آموزشی انبار."""

from dataclasses import dataclass


@dataclass(slots=True)
class InventoryItem:
    """یک قلم کالا و موجودی آن."""

    sku: str
    name: str
    quantity: int = 0

    def increase(self, amount: int) -> None:
        """موجودی را به اندازه مثبت افزایش می‌دهد."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.quantity += amount

    def decrease(self, amount: int) -> None:
        """موجودی را بدون منفی‌شدن کاهش می‌دهد."""
        if amount <= 0 or amount > self.quantity:
            raise ValueError("invalid amount")
        self.quantity -= amount
