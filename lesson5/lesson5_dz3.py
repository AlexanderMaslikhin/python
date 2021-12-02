# Из условия не совсем понятен формат файла
# "построчно записать фамилии сотрудников и величину их окладов"
# Это может означать что каждая величина (фамилия и оклад) в новой строке
# например так:
# Иванов
# 30000
# Петров
# 20000
# Или фамилия и оклад в одной строке с каким то разделителем, например так:
# Иванов 30000
# Петров 20000
#
# Поэтому сделал 2 варианта

def read_var_1(filename):
    employers_salary = {}
    with open(filename, 'r') as f:
        for line in f:
            surname = line.rstrip()
            employers_salary[surname] = float(f.readline().rstrip())
    return employers_salary


def read_var_2(filename):
    employers_salary = {}
    with open(filename, 'r') as f:
        for line in f:
            surname, salary = line.rstrip().split()
            employers_salary[surname] = float(salary)
    return employers_salary


def process(employers_salary):
    less_20 = [name for name, salary in employers_salary.items() if salary < 20000]
    if less_20:
        print('Список сотрудников с окладом менее 20000: ')
        print(*less_20, sep=', ')
    mean = sum(employers_salary.values()) / len(employers_salary)
    print(f'Средняя величина дохода сотрудников: {mean}')


process(read_var_1('dz3a.txt'))
process(read_var_2('dz3b.txt'))
