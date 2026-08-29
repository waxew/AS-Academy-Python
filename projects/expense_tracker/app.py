"""پروژه آموزشی مدیریت هزینه در محیط خط فرمان."""


def total_expenses(expenses: list[float]) -> float:
    """جمع هزینه‌ها را محاسبه می‌کند."""
    return sum(expenses)


if __name__ == "__main__":
    sample_expenses = [120_000, 85_500, 300_000]
    print(f"Total: {total_expenses(sample_expenses):,.0f}")
