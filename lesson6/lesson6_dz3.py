class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


person_1 = Position('Иван', 'Иванов', 'грузчик', 20000., 5000.)
print(person_1.name, person_1.surname, person_1.position)
print(person_1.get_full_name(), person_1.get_total_income())


person_2 = Position('Петр', 'Петров', 'кладовщик', 25000., 10000.)
print(person_2.name, person_2.surname, person_2.position)
print(person_2.get_full_name(), person_2.get_total_income())






