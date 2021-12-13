from random import sample


def create_file(filename, count, lower=1, upper=100):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, sample(range(lower, upper), count))))


def sum_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return sum(map(int, data.split()))


def main():
    filename = input('Введите имя файла: ')
    try:
        lower = int(input('Введите нижнюю границу чисел (целое): '))
        upper = int(input('Введите верхнюю границу чисел (целое): '))
        count = int(input('Введите количество чисел: '))
        create_file(filename, count, lower, upper)
        print(f'Сумма чисел в файле {sum_file(filename)}')
    except ValueError:
        print('Ошибка ввода')


main()
