def print_user_info(**kwargs):
    """
    Печатает переданную информацию в одну строку в формате
    имя_поля_1: значение_поля_1, имя_поля_2: значение_поля_2, ...
    """
    string = ", ".join([f'{key}: {data}' for key, data in kwargs.items()])
    print(string)


def main():
    print_user_info(name='Иван',
                    surname='Иванов',
                    year_of_birth=1990,
                    city='LA',
                    email='ivan@ivanoff.net',
                    phone='+71234567890')


main()