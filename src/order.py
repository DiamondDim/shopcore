from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.product import Product


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с именем и описанием."""

    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description


class Order(BaseEntity):
    """Класс для представления заказа на один товар."""

    def __init__(self, product: "Product", quantity: int) -> None:
        super().__init__(product.name, f"Заказ на {quantity} шт. товара {product.name}")
        self.product: "Product" = product
        self.quantity: int = quantity

    @property
    def total_cost(self) -> float:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_cost} руб."
