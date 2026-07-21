import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
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


def test_product_price_getter(sample_product):
    """Тест геттера для цены."""
    assert sample_product.price == 210000.0


def test_product_price_setter_valid(sample_product):
    """Тест сеттера с валидным значением."""
    sample_product.price = 200000.0
    assert sample_product.price == 200000.0


def test_product_price_setter_negative(capsys):
    """Тест сеттера с отрицательным значением."""
    product = Product("Test", "Desc", 1000.0, 5)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000.0


def test_product_price_setter_zero(capsys):
    """Тест сеттера с нулевым значением."""
    product = Product("Test", "Desc", 1000.0, 5)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000.0


def test_new_product_classmethod():
    """Тест класс-метода new_product."""
    product_data = {
        "name": "Samsung",
        "description": "256GB",
        "price": 180000.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_private_price():
    """Тест что атрибут price приватный."""
    product = Product("Test", "Desc", 1000.0, 5)
    with pytest.raises(AttributeError):
        _ = product.__price


def test_product_str(sample_product):
    """Тест магического метода __str__ для Product."""
    result = str(sample_product)
    assert result == "iPhone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add():
    """Тест магического метода __add__ для Product."""
    product1 = Product("Phone1", "Desc", 100.0, 10)
    product2 = Product("Phone2", "Desc", 200.0, 2)
    result = product1 + product2
    # 100*10 + 200*2 = 1400
    assert result == 1400


def test_product_add_type_error(sample_product):
    """Тест __add__ с некорректным типом."""
    with pytest.raises(TypeError):
        _ = sample_product + 100
