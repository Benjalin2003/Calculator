from src.calc import Calculator

calc = Calculator()

def test_addition():
    assert calc.sum(2,2) == 4
    assert calc.sum(-2, -2) == -4
    assert calc.sum(-2, 2) == 0

def test_devide():
    assert calc.divide(2, 1) == 2
    assert calc.divide(0, 1) == 0
    assert calc.divide(1, 2) == 0.5
    assert calc.divide(2, -2) == -1
    assert calc.divide(-2, -2) == 1

def test_multyply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(2, 0) == 0
    assert calc.multiply(0, -3) == 0
    assert calc.multiply(1, -3) == -3
    assert calc.multiply(-1, -3) == 3
    assert calc.multiply(1.5, 2) == 3
    assert calc.multiply(1.5, -2) == -3

def test_subtract():
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(2, 4) == -2
    assert calc.subtract(2, -4) == 6
    assert calc.subtract(-2, -4) == 2

