import pytest
from lib.shoe import Shoe

def test_shoe_creation():
    s = Shoe("Nike", 10, "Black", 120.0)
    assert s.brand == "Nike"
    assert s.size == 10
    assert s.color == "Black"
    assert s.price == 120.0

def test_invalid_brand():
    with pytest.raises(ValueError):
        Shoe("", 10, "Black", 100)

def test_invalid_size():
    with pytest.raises(ValueError):
        Shoe("Brand", 0, "Color", 50)

    with pytest.raises(TypeError):
        Shoe("Brand", "big", "Color", 50)

def test_invalid_color():
    with pytest.raises(ValueError):
        Shoe("Brand", 10, "", 50)

def test_invalid_price():
    with pytest.raises(ValueError):
        Shoe("Brand", 10, "Color", -10)

    with pytest.raises(TypeError):
        Shoe("Brand", 10, "Color", "expensive")
