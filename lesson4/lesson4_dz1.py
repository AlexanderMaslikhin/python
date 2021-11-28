from sys import argv


def salary(work_time, wage_rate, bonus=0):
    return work_time * wage_rate + bonus


def print_help():
    print("Параметры: <выработка в часах> <ставка в час> [премия (необязательно, по умолчанию 0)]")
    print(f"Пример: {argv[0]} 200 750 30000")
    print("Остальные параметры игнорируются")


def main():
    if len(argv) < 3:
        print_help()
    else:
        try:
            i = 4 if len(argv) >= 4 else 3
            data = list(map(float, argv[1:i]))
            print(f'Заработная плата: {salary(*data)}')
        except ValueError:
            print("Введены некорректные данные")


main()
