# Python Calculator

Консольный калькулятор на Python с поддержкой памяти (M+/M-/MR/MC) и историей вычислений.

## Возможности

- Базовые арифметические операции: сложение, вычитание, умножение, деление
- Защита от деления на ноль с понятным сообщением об ошибке
- Память калькулятора: M+ (прибавить), M- (вычесть), MR (показать), MC (очистить)
- История всех вычислений, включая неудачные попытки деления
- Полное покрытие тестами (pytest)

## Установка

```bash
git clone https://github.com/epif4nov/python-calculator.git
cd python-calculator
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Использование

```bash
python main.py
```

После запуска выберите номер операции из меню:

--- Калькулятор ---

Сложение
Вычитание
Умножение
Деление
M+ (прибавить к памяти)
M- (вычесть из памяти)
MR (показать память)
MC (очистить память)
Показать историю
Выход

## Тесты

```bash
pytest tests/ -v
```

## Структура проекта

python-calculator/
├── calculator/
│ ├── operations.py # арифметические операции
│ ├── memory.py # логика памяти калькулятора
│ ├── history.py # хранение истории вычислений
│ └── cli.py # интерфейс командной строки
├── tests/ # тесты pytest
├── main.py # точка входа
└── requirements.txt


## Технологии

- Python 3.10+ (используется match/case)
- pytest для тестирования