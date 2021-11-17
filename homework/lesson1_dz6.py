start_dist = float(input('Введите начальную дистанцию, км: '))
target_dist = float(input('Введите целевую дистанцию, км: '))

current_dist = start_dist
day_number = 1
print(f'{day_number}-й день: {current_dist}')

while current_dist <= target_dist:
    current_dist *= 1.1
    day_number += 1
    print(f'{day_number}-й день: {current_dist}')

print(f'На {day_number}-й спортсмен достиг результата не менее {target_dist} км')


