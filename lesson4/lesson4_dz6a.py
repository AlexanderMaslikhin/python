from itertools import count


def main():
    print("Создает массив целых чисел в заданном диапазоне с заданным шагом")
    try:
        start = int(input('Введите начальное число - '))
        end = int(input('Введите конечное число - '))
        step = int(input('Введите шаг - '))
        numbers = []
        for elem in count(start, step):
            numbers.append(elem)
            if elem == end:
                break
        print(numbers)
    except ValueError:
        print('Введены некорректные значения')


main()
