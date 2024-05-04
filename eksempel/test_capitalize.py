import capitalize
import pytest

def test_capitalize():
    assert capitalize.capitalize("elvebakken") == "Elvebakken"

def test_capitalize_typeerror():
    with pytest.raises(TypeError):
        capitalize.capitalize(123)