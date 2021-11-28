from random import randrange
from itertools import cycle


def main():
    """
    Повторяет элементы заданного списка
    Размеры заданного и конечного списков задаются пользователем
    Исходный список создается песвдослучайно
    """
    try:
        start_len = int(input('Размер исходного списка - '))
        result_len = int(input('Введите размер конечного списка - '))
        start_list = [randrange(100) for _ in range(start_len)]
        result_list = []
        for i, elem in enumerate(cycle(start_list), 1):
            result_list.append(elem)
            if i == result_len:
                break
        print(start_list, result_list, sep="\n")
    except ValueError:
        print('Введены некорректные данные')


main()