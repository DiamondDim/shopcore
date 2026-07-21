import pytest
from src.smartphone import Smartphone
from src.product import Product
from src.lawn_grass import LawnGrass


@pytest.fixture
def sample_smartphone():
    return Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")


def test_smartphone_initialization(sample_smartphone):
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "S23"


def test_smartphone_is_product(sample_smartphone):
    assert isinstance(sample_smartphone, Product)


def test_smartphone_add_same_class():
    phone1 = Smartphone("P1", "D", 100.0, 10, 90.0, "M1", 128, "B")
    phone2 = Smartphone("P2", "D", 200.0, 2, 85.0, "M2", 256, "W")
    assert phone1 + phone2 == 1400.0


def test_smartphone_add_different_class():
    phone = Smartphone("P1", "D", 100.0, 10, 90.0, "M1", 128, "B")
    grass = LawnGrass("G", "D", 50.0, 5, "RU", "7", "G")
    with pytest.raises(TypeError):
        _ = phone + grass
