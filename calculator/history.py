class History:
    """Хранит историю операций и их результатов"""

    def __init__(self) -> None:
        """Начальный пустой список истории"""
        self._entries: list[str] = []

    def add_entry(self, entry: str) -> None:
        """Добавляет новое значение в историю"""
        self._entries.append(entry)

    def get_all(self) -> list[str]:
        """Выводит текущее значение из истории"""
        return self._entries

    def clear(self) -> None:
        """Удаляет предыдущие записи из истории"""
        self._entries = []