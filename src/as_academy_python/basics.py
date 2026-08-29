"""مثال‌های پایه دوره Python.

توابع این فایل کوچک و قابل تست نگه داشته شده‌اند تا هنرجو هم‌زمان
با Syntax پایتون، اصول نوشتن کد قابل نگهداری را نیز یاد بگیرد.
"""


def greet(name: str) -> str:
    """یک پیام خوش‌آمدگویی برای نام دریافت‌شده برمی‌گرداند."""
    clean_name = name.strip() or "Python Learner"
    return f"Hello, {clean_name}!"


def calculate_discount(price: float, percent: float) -> float:
    """قیمت نهایی را پس از اعمال درصد تخفیف محاسبه می‌کند."""
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return price * (1 - percent / 100)


def celsius_to_fahrenheit(celsius: float) -> float:
    """دمای سلسیوس را به فارنهایت تبدیل می‌کند."""
    return (celsius * 9 / 5) + 32
