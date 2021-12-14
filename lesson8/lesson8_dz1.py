days_of_mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


class Date:
    def __init__(self, date_string):
        self.day, self.mon, self.year = 1, 1, 1975
        try:
            nums = Date.convert_to_num(date_string)
            if Date.data_validation(nums):
                self.day, self.mon, self.year = nums
            else:
                raise ValueError
        except ValueError:
            print(f'Ошибка преобразования даты. {date_string} неверный формат')

    @classmethod
    def convert_to_num(cls, date_string):
        return tuple(map(int, date_string.split('-')))

    @staticmethod
    def data_validation(nums):
        if len(nums) == 3:
            day, mon, year = nums
            if 0 < mon < 13:
                if year >= 0:
                    num_days = days_of_mon[mon]
                    if not year % 4:
                        num_days += 1
                    if 0 < day <= num_days:
                        return True
        return False

    def __str__(self):
        return f'{self.day:02}.{self.mon:02}.{self.year}'


date = Date('01-01-2021')
print(date)
wrong_date_1 = Date('казя-базя')
wrong_date_2 = Date('32-13-2020')
