# نصب و راه‌اندازی

1. Python 3.11 یا جدیدتر را نصب کنید.
2. صحت نصب را با `python --version` یا `python3 --version` بررسی کنید.
3. محیط مجازی بسازید: `python -m venv .venv`.
4. محیط را فعال کنید.
5. برای توسعه: `pip install -e .[dev]`.
6. تست‌ها: `pytest`.
7. بررسی lint: `ruff check .`.

در Windows هنگام نصب رسمی Python گزینه افزودن Python به PATH باید فعال باشد.
