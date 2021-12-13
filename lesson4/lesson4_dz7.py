def fact(n):
    start = 1
    for i in range(1, n + 1):
        start *= i
        yield start


def main():
    """
    Получение факториалов чисел с помощью генератора
    """
    try:
        end_number = int(input('Введите до какого числа включительно нужны факториалы - '))
        for k in fact(end_number):
            print(k, end=' ')
    except ValueError:
        print("Введены некорректные данные")


main()
