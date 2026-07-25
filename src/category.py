from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута списка товаров."""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию с проверкой типа."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты Product и его наследников")

    def __str__(self):
        """Строковое представление категории с общим количеством товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self):
        return f"Category('{self.name}', '{self.description}', {self.__products})"
