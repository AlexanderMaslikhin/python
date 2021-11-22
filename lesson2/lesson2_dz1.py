var_list = [10, 9., complex(8, 7), '654', [3, 2], (1, 0), {'a': 'b', 'c': 'd'}, {'e', 'f'}]

for elem in var_list:
    print(f'Тип текущего элемента списка: {elem} => {type(elem)}')
