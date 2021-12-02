import json


def read_file(filename):
    firms_profit = {}
    profit_sum = 0
    good_firms_count = 0
    with open(filename, 'r') as f:
        for line in f:
            name, jur_status, proceeds, spending = line.strip().split()
            firms_profit[name] = float(proceeds) - float(spending)
            if firms_profit[name] > 0:
                profit_sum += firms_profit[name]
                good_firms_count += 1

    return [firms_profit, {'average_profit': profit_sum/good_firms_count}]


def export_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


data = read_file('dz7.txt')
print(data)
export_json('firms.json', data)

