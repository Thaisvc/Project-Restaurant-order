from src.models.ingredient import Ingredient


# Req 1
def test_ingredient():
    instance_test_1 = Ingredient('manteiga')
    instance_test_2 = Ingredient('alho')

    assert instance_test_1 == instance_test_1
    assert instance_test_1 != instance_test_2
    assert hash(instance_test_1) == hash(instance_test_1)
    assert hash(instance_test_1) != hash(instance_test_2)
    assert repr(instance_test_2) == "Ingredient('alho')"
    assert instance_test_2.name == "alho"
    assert instance_test_2.restrictions == set()
