from src.product import Product
from src.category import Category


def test_add_product_success_messages(capsys):
    """Проверка успешного добавления товара с выводом сообщений (else/finally)."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание", [])

    category.add_product(product)

    captured = capsys.readouterr()
    assert "Товар успешно добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_add_product_zero_quantity_messages(capsys):
    """Проверка обработки товара с нулевым количеством при добавлении."""
    # Создаем валидный товар, чтобы обойти проверку в __init__
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание", [])

    # Искусственно обнуляем количество для проверки защиты в add_product
    product.quantity = 0

    category.add_product(product)

    captured = capsys.readouterr()
    assert "нулевым количеством" in captured.out
    assert "Обработка добавления товара завершена" in captured.out
