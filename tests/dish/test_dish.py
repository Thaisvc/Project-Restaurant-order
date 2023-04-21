from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    test_1 = Dish("camarão", 21.30)
    test_2 = Dish("tomate", 2.50)
    assert test_1.name == "camarão"
    assert test_1.__repr__() == "Dish('camarão', R$21.30)"
    assert test_1.__hash__() != test_2.__hash__()
    assert test_1.__hash__() == test_1.__hash__()
    assert test_1.__eq__(test_1)
    assert not test_1.__eq__(test_2)

    with pytest.raises(TypeError):
        Dish("camarão", " 21.30")

    with pytest.raises(ValueError):
        Dish("camarão", 0)

    instance = Ingredient("mamão")
    test_1.add_ingredient_dependency(instance, 2)

    assert test_1.get_ingredients() == {instance}
    assert test_1.get_restrictions() == set(instance.restrictions)
