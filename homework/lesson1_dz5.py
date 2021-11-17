proceeds = float(input('Введите объем выручки в рублях:'))
spending = float(input('Введите объем затрат в рублях:'))

profit = proceeds - spending

if profit < 0:
    print('Упс! Ваше фирма убыточна. Надо что то менять!')

elif profit > 0:
    rent = profit / proceeds
    print(f'Ваша фирма приносит прибыль {profit} руб. Рентабельность составляет {int(rent * 100)}%')
    employers_count = int(input('Введите количество сотрудников: '))
    profit_per_employer = profit / employers_count
    print(f'Прибыль на одного сотрудника составляет {profit_per_employer} руб.')

else:  # profit == 0
    print('Прибыли нет но и убытков тоже нет. Работа ради работы???')
