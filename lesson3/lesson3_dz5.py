# чтобы не писать заново импортирую из первой задачи
from lesson3_dz1 import is_numbers


def is_data_correct(data):
    """
    Проверяет корректность введенной строки с числами
    """
    num_list = data.split()
    return is_numbers(*num_list)


def get_input():
    """Запрашивает ввод и возвращает введенную строку"""
    return input('Введите числа через пробел. Для выхода введите "q" - ')


def get_sum_from_str(str_data):
    """
    Суммирует введенные числа
    если строка пустая, то split вернет пустой список.
    sum от пустого списка возвращает 0
    """
    numbers = map(float, str_data.split())
    return sum(numbers)


def main():
    summa = 0
    end = False
    while not end:
        next_string = get_input()
        if 'q' in next_string:
            next_string, *_ = next_string.split('q')
            next_string = next_string.rstrip()
            end = True
        if not is_data_correct(next_string):
            print('Ошибка! Повторите ввод')
            end = False
            continue
        summa = summa + get_sum_from_str(next_string)
        print(f'Сумма введенных чисел: {summa}')

    print('The End!')


main()
