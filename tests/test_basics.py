from as_academy_python.basics import calculate_discount, celsius_to_fahrenheit, greet


def test_greet() -> None:
    assert greet("Ali") == "Hello, Ali!"


def test_discount() -> None:
    assert calculate_discount(100_000, 20) == 80_000


def test_temperature() -> None:
    assert celsius_to_fahrenheit(0) == 32
