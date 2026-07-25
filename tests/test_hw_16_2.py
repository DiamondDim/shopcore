import pytest
from src.product import Product, BaseProduct
from src.order import Order, BaseEntity
from src.category import Category


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100, 1)


def test_print_repr_mixin(capsys):
    product = Product("Тест", "Описание", 100, 1)
    captured = capsys.readouterr()
    assert product.name == "Тест"
    assert "Product('Тест', 'Описание', 100, 1)" in captured.out


def test_order_creation():
    product = Product("Телефон", "Смартфон", 50000, 2)
    order = Order(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.total_cost == 100000
    assert isinstance(order, BaseEntity)


def test_category_inherits_base_entity():
    category = Category("Тест", "Описание", [])
    assert isinstance(category, BaseEntity)
