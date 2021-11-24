def int_func(word):
    """Изменяет первую букву слова на заглавную"""
    return word.capitalize()


def inc_func_all(string):
    """Изменяет первые буквы на заглавные у всех слов строки"""
    return ' '.join(map(int_func, string.split()))


def main():
    string = input("Введите несколько слов через пробел - ")
    print(f'Итоговая строка: {inc_func_all(string)}')


main()