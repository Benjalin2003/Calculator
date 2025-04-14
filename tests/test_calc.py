import pytest

from src.calc import Calculator

calc = Calculator()

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (-2, 2, 0),
        (-2, -2, -4),
    ]
)

def test_sum(a, b, expected):
    """Проверка сложения"""
    assert calc.sum(a, b) == expected

@pytest.mark.parametrize(
    "a1, b1, expected1",
    [
        (2, 1, 2),
        (0, 1, 0),
        (1, 2, 0.5),
        (2, -2, -1),
        (-2, -2, 1),
    ]
)

def test_devide(a1, b1, expected1):
    assert calc.divide(a1, b1) == expected1

@pytest.mark.parametrize(
    "a2, b2, expected2",
    [
        (2, 3, 6),
        (2, 0, 0),
        (0, -3, 0),
        (1, -3, -3),
        (-1, -3, 3),
        (1.5, 2, 3),
        (1.5, -2, -3),
    ]
)

def test_multiply(a2, b2, expected2):
    assert calc.multiply(a2, b2) == expected2

@pytest.mark.parametrize(
    "a3, b3, expected3",
    [
        (2, 1, 1),
        (2, 4, -2),
        (2, -4, 6),
        (-2, -4, 2),
    ]
)

def test_substract(a3, b3, expected3):
    assert calc.subtract(a3, b3) == expected3