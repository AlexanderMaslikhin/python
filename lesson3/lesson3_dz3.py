# чтобы не писать заново импортирую из первой задачи
from lesson3_dz1 import is_numbers


def my_func(num1, num2, num3):
    """
    Возвращает сумму из двух наибольших аргументов
    Агрументы должны быть числа
    """
    num_list = [num1, num2, num3]
    num_list.pop(num_list.index(min(num_list)))
    return sum(num_list)


# проверка
def main():
    while True:
        num1, num2, num3 = input('Введите три числа через пробел - ').split()
        if is_numbers(num1, num2, num3):
            print(my_func(float(num1), float(num2), float(num3)))
            break
        print('Ошибка! Повторите попытку')


main()
