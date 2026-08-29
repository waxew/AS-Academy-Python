"""نمونه ساده OOP برای دوره پیشرفته."""

from dataclasses import dataclass


@dataclass(slots=True)
class Product:
    """مدل آموزشی یک محصول."""

    name: str
    price: float
    stock: int = 0

    def sell(self, quantity: int) -> float:
        """موجودی را کاهش داده و مبلغ فروش را برمی‌گرداند."""
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if quantity > self.stock:
            raise ValueError("insufficient stock")
        self.stock -= quantity
        return self.price * quantity
