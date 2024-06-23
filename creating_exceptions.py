class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def process(num):
    if num < 0:
        raise InvalidDataException("Данные неверны, введите положительное число")
    if num % 2 == 1:
        raise ProcessingException("Данные неверны, число должно быть четным")
    else:
        return "Данные введены верно"


for _ in range(1, int(input("Введите число от 1 до 9: ")) + 1):
    num = int(input("Введите число: "))
    try:
        res = process(num)
        print(f"Результат обработки данных {num}: {res}")
    except (InvalidDataException, ProcessingException) as e:
        print(f"Ошибка: {e}")
    finally:
        print(f"Завершение обработки.\n")

