import pytest
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def sample_grass():
    return LawnGrass("Трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_lawn_grass_initialization(sample_grass):
    assert sample_grass.country == "Россия"
    assert sample_grass.germination_period == "7 дней"


def test_lawn_grass_is_product(sample_grass):
    assert isinstance(sample_grass, Product)


def test_lawn_grass_add_different_class():
    grass = LawnGrass("G", "D", 50.0, 5, "RU", "7", "G")
    phone = Smartphone("P1", "D", 100.0, 10, 90.0, "M1", 128, "B")
    with pytest.raises(TypeError):
        _ = grass + phone
