from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self._price: float = price
        self.quantity: int = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @abstractmethod
    def get_product_info(self) -> str:
        """Абстрактный метод для получения информации о продукте."""
        pass

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class PrintReprMixin:
    """Миксин для вывода информации о создании объекта в консоль."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        args_repr = ", ".join(
            [repr(arg) for arg in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()]
        )
        print(f"{self.__class__.__name__}({args_repr})")
        super().__init__(*args, **kwargs)


class Product(PrintReprMixin, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def get_product_info(self) -> str:
        """Реализация абстрактного метода для получения информации о продукте."""
        return f"{self.name}: {self.description}, цена {self.price} руб., остаток {self.quantity} шт."

    def __repr__(self) -> str:
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)
