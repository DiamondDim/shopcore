import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов."""
    return [
        Product("iPhone 15", "512GB", 210000.0, 8),
        Product("Samsung S23", "256GB", 180000.0, 5)
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории."""
    return Category("Смартфоны", "Мобильные телефоны", sample_products)


def test_category_initialization(sample_category):
    """Тест корректной инициализации объекта Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Мобильные телефоны"
    # Теперь products — это строка, поэтому проверяем через приватный атрибут
    assert len(sample_category._Category__products) == 2


def test_category_products_are_product_objects(sample_category):
    """Тест что список содержит объекты Product."""
    for product in sample_category._Category__products:
        assert isinstance(product, Product)


def test_category_count_increment():
    """Тест автоматического подсчёта количества категорий."""
    Category.category_count = 0
    Category.product_count = 0

    products1 = [Product("Phone1", "Desc", 1000.0, 2)]
    products2 = [Product("Phone2", "Desc", 2000.0, 3)]

    Category("Cat1", "Desc1", products1)
    Category("Cat2", "Desc2", products2)

    assert Category.category_count == 2


def test_product_count_increment():
    """Тест автоматического подсчёта количества товаров."""
    Category.category_count = 0
    Category.product_count = 0

    products1 = [Product("Phone1", "Desc", 1000.0, 2)]
    products2 = [Product("Phone2", "Desc", 2000.0, 3), Product("Phone3", "Desc", 3000.0, 1)]

    Category("Cat1", "Desc1", products1)
    Category("Cat2", "Desc2", products2)

    assert Category.product_count == 3


def test_category_attributes_types(sample_category):
    """Тест типов данных атрибутов Category."""
    assert isinstance(sample_category.name, str)
    assert isinstance(sample_category.description, str)
    # products теперь возвращает строку через геттер
    assert isinstance(sample_category.products, str)


def test_category_products_getter(sample_category):
    """Тест геттера для списка товаров."""
    result = sample_category.products
    assert "iPhone 15" in result
    assert "210000.0 руб." in result
    assert "Остаток: 8 шт." in result


def test_category_add_product(sample_category):
    """Тест метода add_product."""
    initial_count = Category.product_count
    new_product = Product("New Phone", "Desc", 50000.0, 3)
    sample_category.add_product(new_product)
    assert Category.product_count == initial_count + 1


def test_category_products_private():
    """Тест что атрибут products приватный."""
    category = Category("Test", "Desc", [])
    with pytest.raises(AttributeError):
        _ = category.__products
