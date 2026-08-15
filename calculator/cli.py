from calculator.operations import add, subtract, multiply, divide, DivisionByZeroError

def get_two_numbers() -> tuple[float, float]:
    """Запрашивает у пользователя два числа и возвращает их парой"""
    a = float(input("Введите первое число:"))
    b = float(input("Введите второе число:"))
    return a, b

def run() -> None:
    """Запускает основной цикл калькулятора."""
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
                print(add(a, b))

            case '2':
                a, b = get_two_numbers()
                print(subtract(a, b))

            case '3':
                a, b = get_two_numbers()
                print(multiply(a, b))

            case '4':
                a, b = get_two_numbers()
                try:
                    print(divide(a, b))
                except DivisionByZeroError:
                    print("Ошибка: деление на ноль недопустимо")

            case _:
                print("Пока не реализовано")

if __name__ == "__main__":
    run()