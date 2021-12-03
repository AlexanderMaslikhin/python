list_1 = input('Введите элементы списка через пробел: ').split(' ')
print(f'Введенный список: {list_1}')

last_idx = -(len(list_1) % 2) or None

list_1[:last_idx:2], list_1[1:last_idx:2] = list_1[1:last_idx:2], list_1[:last_idx:2]
print(f'Итоговый список: {list_1}')
