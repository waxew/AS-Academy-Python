from as_academy_python.collections_examples import unique_sorted, word_frequency


def test_unique_sorted() -> None:
    assert unique_sorted([3, 1, 3, 2]) == [1, 2, 3]


def test_word_frequency() -> None:
    assert word_frequency("Python python Academy") == {"python": 2, "academy": 1}
