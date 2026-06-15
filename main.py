from src.product import Product
from src.category import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Тест __str__ для Product
    print(product1)
    print(product2)
    print(product3)

    # Тест __str__ для Category
    print(category1)

    # Тест геттера products (теперь использует __str__)
    print(category1.products)

    # Тест __add__
    print(product1 + product2)  # 180000*5 + 210000*8 = 2580000

    # Тест new_product
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0, "quantity": 5}
    )
    print(new_product)

    # Тест сеттера цены
    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
