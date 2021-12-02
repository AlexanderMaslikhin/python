
def get_sum(line):
    ## вычищаем все лишнее
    numbers = ''.join(filter(lambda x: x.isdigit() or x == ' ', line)).split()
    return sum(map(int, numbers))


def parse_file(filename):
    subjects_hours = {}
    with open(filename, 'r') as f:
        for line in f:
            subject, rest = line.split(": ")
            subjects_hours[subject] = get_sum(rest.strip())

    return subjects_hours


print(parse_file('dz6.txt'))



