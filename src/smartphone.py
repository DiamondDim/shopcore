from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone('{self.name}', '{self.description}', {self.price}, "
                f"{self.quantity}, {self.efficiency}, '{self.model}', {self.memory}, '{self.color}')")
