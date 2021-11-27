from functools import reduce

# хотел сделать так
# even_numbers = list(range(100, 1001, 2))

# но нужно использовать возможности 'генератора'
even_numbers = [elem for elem in range(100, 1001, 2)]

# Ооооочень большое число)
print(reduce(lambda prev_num, next_num: prev_num * next_num, even_numbers))

