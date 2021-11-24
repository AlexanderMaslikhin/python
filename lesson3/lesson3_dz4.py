# чтобы не писать заново импортирую из первой задачи
from lesson3_dz1 import is_numbers


def pow_operator(x, y):
    """
    Возводит x в степень y используя оператор **
    x - действительное положительно число, y - целое отрицательное
    """
    return x ** y


def pow_cycle(x, y):
    """
    Возводит x в степень y, используя цикл
    x - действительное положительно число, y - целое отрицательное
    """
    res = 1
    for _ in range(abs(y)):
        res /= x
    return res


def main():
    while True:
        x, y = input('Введите через пробел положительное действительное число и целое отрицательное число - ').split()
        if is_numbers(x) and float(x) > 0 and y.replace('-', '').isdigit() and int(y) < 0:
            print(f'Степень через оператор:', pow_operator(float(x), int(y)))
            print(f'Степень через цикл:', pow_cycle(float(x), int(y)))
            break
        print('Ошибка! Повторите попытку')


main()
