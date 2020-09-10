from fizzbuzz import fizzbuzz

import pytest


@pytest.mark.parametrize("arg, expected", [
    (3, "Fizz"),
    (33, "Fizz"),
    (69, "Fizz"),
    (5, "Buzz"),
    (65, "Buzz"),
    (85, "Buzz"),
    (15, "Fizz Buzz"),
    (45, "Fizz Buzz"),
    (11, 11),
    (59, 59),
    (94, 94)
])
def test_fizzbuzz(arg, expected):
    assert fizzbuzz(arg) == expected
