class NotNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
while True:
    try:
        next_num = input("введите число или 'q' для выхода - ")
        if not next_num.isdigit():
            raise NotNumberException(next_num)
        else:
            num_list.append(int(next_num))
    except NotNumberException as e:
        if e.txt == 'q':
            break
        else:
            print("Ошибка ввода! Нужно вводить только числа или q для выхода!")

print(num_list)
