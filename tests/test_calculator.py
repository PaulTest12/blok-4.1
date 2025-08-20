import pytest
from app.calculator import add, sub, mul, div

def test_addition():
    assert add(2, 3) == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_mul_and_sub():
    assert sub(mul(4, 3), 5) == 7
