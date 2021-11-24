def division(numerator, denominator):
    """ Выполняет деление 2х чисел """
    return numerator / denominator


def is_numbers(*args):
    """ Проверяет корректность введенных чисел.
    Возвращает True если все данные числа, иначе False """
    for number in args:
        try:
            float(number)
        except ValueError:
            return False
    return True


def main():
    while True:
        numerator, denominator = input('Введите делимое и делитель через пробел - ').split()
        if not is_numbers(numerator, denominator):
            print('Введены ошибочные данные. Повторите попытку')
            continue
        elif float(denominator):
            break
        else:
            print('Ошибка. На ноль делить нельзя. Повторите попытку')

    print(f'Частное этих чисел {division(float(numerator), float(denominator))}')


if __name__ == '__main__':  # Это для следующих заданий, чтобы импортить функцию проверки на числа is_numbers
    main()
