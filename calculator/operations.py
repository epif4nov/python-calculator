class DivisionByZeroError(Exception):
    """Исключение, возникающее при попытке деления на ноль."""
    pass

def add(a: float, b: float) -> float:
    """Возвращает сумму a и b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Возвращает разность a и b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Возвращает произведение a и b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Возвращает частное от деления a на b."""
    if b == 0:
        raise DivisionByZeroError("division by zero")
    return a / b