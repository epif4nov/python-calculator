from calculator.operations import add, subtract, multiply, divide, DivisionByZeroError
from calculator.memory import Memory
from calculator.history import History

def get_two_numbers() -> tuple[float, float]:
    """Запрашивает у пользователя два числа и возвращает их парой"""
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b

def run() -> None:
    """Запускает основной цикл калькулятора."""
    memory = Memory()
    history = History()

    while True:
        print("\n--- Калькулятор ---")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. M+ (прибавить к памяти)")
        print("6. M- (вычесть из памяти)")
        print("7. MR (показать память)")
        print("8. MC (очистить память)")
        print("9. Показать историю")
        print("0. Выход")

        choice = input("Выберите действие: ")

        match choice:
            case '0':
                print("До свидания!")
                break
            case '1':
                a, b = get_two_numbers()
                result = add(a, b)
                history.add_entry(f"{a} + {b} = {result}")
                print(result)

            case '2':
                a, b = get_two_numbers()
                result = subtract(a, b)
                history.add_entry(f"{a} - {b} = {result}")
                print(result)

            case '3':
                a, b = get_two_numbers()
                result = multiply(a, b)
                history.add_entry(f"{a} * {b} = {result}")
                print(result)

            case '4':
                a, b = get_two_numbers()
                try:
                    result = divide(a, b)
                    history.add_entry(f"{a} / {b} = {result}")
                    print(result)
                except DivisionByZeroError:
                    history.add_entry(f"{a} / {b} = ошибка (деление на ноль)")
                    print("Ошибка: деление на ноль недопустимо")

            case '5':
                value = float(input("Введите число: "))
                memory.add(value)
                print(f"Текущее значение памяти: {memory.recall()}")

            case '6':
                value = float(input("Введите число: "))
                memory.subtract(value)
                print(f"Текущее значение памяти: {memory.recall()}")

            case '7':
                value = memory.recall()
                print(f"Текущее число: {value}")

            case '8':
                memory.clear()
                print("Память очищена")

            case '9':
                entries = history.get_all()
                if entries:
                    for entry in entries:
                        print(entry)
                else:
                    print("История пуста")


            case _:
                print("Пока не реализовано")

if __name__ == "__main__":
    run()