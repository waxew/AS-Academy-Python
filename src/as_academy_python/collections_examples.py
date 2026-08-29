"""نمونه‌های آموزشی ساختمان داده‌ها."""


def unique_sorted(values: list[int]) -> list[int]:
    """مقادیر تکراری را حذف و خروجی را مرتب می‌کند."""
    return sorted(set(values))


def word_frequency(text: str) -> dict[str, int]:
    """تعداد تکرار هر کلمه را محاسبه می‌کند."""
    result: dict[str, int] = {}
    for word in text.lower().split():
        result[word] = result.get(word, 0) + 1
    return result
