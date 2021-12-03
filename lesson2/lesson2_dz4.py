word_list = input('Введите несколько слов через пробел: ').split(' ')

for i, word in enumerate(word_list, 1):
    print(f'{i} {word[:10]}')

