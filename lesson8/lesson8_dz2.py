class DivByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt



try:
    numerator = int(input('Введите делимое - '))
    denominator = int(input('Введите делитель - '))
    if denominator == 0:
        raise DivByZeroException("На ноль делить нельзя")
except ValueError:
    print("Введены некорректные данные")
except DivByZeroException as e:
    print(e)
else:
    print(f'Частное = {numerator / denominator}')
