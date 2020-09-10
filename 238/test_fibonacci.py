from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_


def test_fib_zero():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib_seven():
    assert fib(7) == 13


def test_fib_ten():
    assert fib(10) == 55


def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-1)
