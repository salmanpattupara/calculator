from calculator import addition, division, multiplication, subtraction


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0


def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(10, 7) == 3


def test_multiplication():
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 5) == -10


def test_division():
    assert division(10, 4) == 2.5
    assert division(1, 3) == 0.33
    assert division(5, 0) == "division by zero not permissible"
