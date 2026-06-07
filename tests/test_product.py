import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("iPhone 15", "512GB, Gray", 210000.0, 8)


def test_product_initialization(sample_product):
    """Тест корректной инициализации объекта Product."""
    assert sample_product.name == "iPhone 15"
    assert sample_product.description == "512GB, Gray"
    assert sample_product.price == 210000.0
    assert sample_product.quantity == 8


def test_product_attributes_types(sample_product):
    """Тест типов данных атрибутов Product."""
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, float)
    assert isinstance(sample_product.quantity, int)


def test_product_different_values():
    """Тест создания продукта с разными значениями."""
    product = Product("Samsung", "256GB", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.price == 180000.0
    assert product.quantity == 5
