num = int(input("Введите целое положительное число: "))

# Тут нужно сделать проверку на корректность введенной строки, типа num.isdigit()
# Но мы ведь это еще не проходили ))) Поэтому сразу приводим к целому.

digit = 0

while num > 0:
    if digit < num % 10:
        digit = num % 10
    num //= 10

print(f'Самая большая цифра числа: {digit}')


