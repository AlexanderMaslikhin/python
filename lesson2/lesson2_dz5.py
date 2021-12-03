my_list = [7, 5, 3, 3, 2]

print(f'Текущий рейтинг: {my_list}')

while True:
    inp = input('Введите число или q для выхода: ')
    if inp == 'q':
        break
    my_list.append(int(inp))
    my_list = sorted(my_list, reverse=True)
    print(f'Текущий рейтинг: {my_list}')




