import pytest
from calculator.operations import add, subtract, multiply, divide, DivisionByZeroError

def test_add():
    """Тест на операцию сложения"""
    assert add(1, 2) == 3

def test_subtract():
    """Тест на операцию вычитания"""
    assert subtract(1, 2) == -1

def test_multiply():
    """Тест на операцию умножения"""
    assert multiply(2, 3) == 6

def test_divide():
    """Тест на успешную операцию деления"""
    assert divide(9,3) == 3

def test_divide_by_zero():
    """Тест ошибки деления на ноль"""
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)