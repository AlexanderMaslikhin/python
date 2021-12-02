
def main():
    filename = input('Введите имя файла: ')
    with open(filename, 'w') as f:
        data = None
        while data != '':
            data = input('Введите строку для записи в файл или пустую строку для выхода: ')
            f.write(data + '\n')


main()
