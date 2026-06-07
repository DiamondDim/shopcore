import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_products():
    return [
        Product("iPhone 15", "512GB", 210000.0, 8),
        Product("Samsung S23", "256GB", 180000.0, 5)
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Смартфоны", "Мобильные телефоны", sample_products)


def test_category_initialization(sample_category):
    """Тест корректной инициализации объекта Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Мобильные телефоны"
    assert len(sample_category.products) == 2


def test_category_products_are_product_objects(sample_category):
    """Тест что список содержит объекты Product."""
    for product in sample_category.products:
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
    assert isinstance(sample_category.products, list)
