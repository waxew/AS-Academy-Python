from as_academy_python.oop import Product


def test_product_sale() -> None:
    product = Product("Book", 10, 3)
    assert product.sell(2) == 20
    assert product.stock == 1
