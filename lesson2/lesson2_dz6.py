# Вводим данные

goods_count = int(input('Введите количество товаров: '))

goods = []

for i in range(1, goods_count + 1):
    good_dict = {'название': input(f"Введите название {i}-го товара: "),
                 'цена': float(input(f'Введите цену {i}-го товара: ')),
                 'количество': float(input(f'Введите количество {i}-го товара: ')),
                 'ед': input(f'Введите единицу измерения {i}-го товара: ')}
    goods.append((i, good_dict))

# Анализируем данные

itog = {key: list(set([item[key] for i, item in goods])) for key in goods[0][1].keys()}

print(*(itog.items()), sep='\n')
