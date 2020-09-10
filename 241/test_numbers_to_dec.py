import pytest

from numbers_to_dec import list_to_decimal


def test_correct():
    assert list_to_decimal([0, 4, 2, 8]) == 428
    assert list_to_decimal([1, 2]) == 12
    assert list_to_decimal([5, 2, 3, 5, 4, 2, 1]) == 5235421
    assert list_to_decimal([2, 1, 3]) == 213
    assert list_to_decimal([1, 0, 5, 0, 2]) == 10502
    assert list_to_decimal([1]) == 1


@pytest.mark.parametrize("wrong_types", [
    [6, 2, True],
    ['hello', 2, 7],
    [9.1, 8, 3, 6, 5],
    [5, 1, 3, 9.2]
])
def test_type_errors(wrong_types):
    with pytest.raises(TypeError):
        list_to_decimal(wrong_types)


@pytest.mark.parametrize("wrong_values", [
    [23, 1, 3],
    [-1, 2, 4],
    [100, 2, 3],
    [11, 5],
    [10, 4, 3, 2, 7]
])
def test_value_errors(wrong_values):
    with pytest.raises(ValueError):
        list_to_decimal(wrong_values)
