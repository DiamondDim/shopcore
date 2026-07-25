from typing import List

from src.exceptions import ZeroQuantityError
from src.order import BaseEntity
from src.product import Product


class Category(BaseEntity):
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        super().__init__(name, description)
        self.__products: List[Product] = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в категорию с обработкой исключений."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты Product и его наследников")

            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

        except (TypeError, ZeroQuantityError) as e:
            print(f"Ошибка: {e}")
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута списка товаров."""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def middle_price(self) -> float:
        """Возвращает среднюю цену всех товаров в категории.
        Если товаров нет — возвращает 0.0."""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    def __str__(self) -> str:
        """Строковое представление категории с общим количеством товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:
        return f"Category('{self.name}', '{self.description}', {self.__products})"
