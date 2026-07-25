from typing import List

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
        """Метод для добавления продукта в категорию с проверкой типа."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты Product и его наследников")

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута списка товаров."""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def __str__(self) -> str:
        """Строковое представление категории с общим количеством товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:
        return f"Category('{self.name}', '{self.description}', {self.__products})"
