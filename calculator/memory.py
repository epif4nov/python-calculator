class Memory:
    """Хранит одно число и поддерживает операции M+/M-/MR/MC."""

    def __init__(self) -> None:
        """Инициализирует память нулевым значением."""
        self._value = 0.0

    def add(self, value: float) -> None:
        """Прибавляет value к памяти (M+)."""
        self._value += value

    def subtract(self, value: float) -> None:
        """Вычитает value из памяти (M-)."""
        self._value -= value

    def recall(self) -> float:
        """Возвращает текущее значение памяти (MR)."""
        return self._value

    def clear(self) -> None:
        """Сбрасывает память в 0 (MC)."""
        self._value = 0.0