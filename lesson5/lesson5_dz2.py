# первый вариант
def var_1(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            print(f'В {i}-й строке {len(line.split())} слов')
    print(f'В файле {i} строк')


# второй вариант
def var_2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    print(f'В файле {len(lines)} строк')
    for i, line in enumerate(lines, 1):
        print(f'В {i}-й строке {len(line.split())} слов')


# третий вариант
def var_3(filename):
    with open(filename, 'r') as f:
        data = f.read()
    lines = data.split('\n')
    print(f'В файле {len(lines)} строк')
    for i, line in enumerate(lines, 1):
        print(f'В {i}-й строке {len(line.split())} слов')


var_1('text.txt')
print("------")
var_2('text.txt')
print("------")
var_3('text.txt')
