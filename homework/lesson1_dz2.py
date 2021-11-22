full_seconds = int(input("Введите количество секунд: "))

seconds = full_seconds % 60
minutes = full_seconds // 60 % 60
hours = full_seconds // 3600

print("Это соответствует {:02}:{:02}:{:02}".format(hours, minutes, seconds))
