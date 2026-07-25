class ZeroQuantityError(ValueError):
    """Пользовательское исключение для попытки добавления товара с нулевым количеством."""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        super().__init__(message)
