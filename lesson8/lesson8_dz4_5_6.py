from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @classmethod
    def get_type(cls):
        return cls.__name__

    def __getattr__(self, item):
        if item == 'type':
            return self.get_type()
        elif item == 'fullname':
            return f'{self.name} {self.model}'

    @abstractmethod
    def work(self):
        pass


class Printer(OfficeEquipment):

    def work(self):
        print("I'm printing")


class Scanner(OfficeEquipment):

    def work(self):
        print("I'm scanning")


class Copier(OfficeEquipment):

    def work(self):
        print("I'm copying")


class Warehouse:
    """
    Общая страктура для склада:
    Три типа оборудования.
    В каждом словарь где ключ - это полное наименование, а значение - количество этого наименования
    """

    __office_eq = {'Printer': {}, 'Scanner': {}, 'Copier': {}}

    @staticmethod
    def items_income(count, item):
        print(f'Поступление на склад {item.type} {item.fullname} в количестве {count} шт.')
        if isinstance(count, int):
            if item.fullname in Warehouse.__office_eq[item.type]:
                Warehouse.__office_eq[item.type][item.fullname] += count
            else:
                Warehouse.__office_eq[item.type][item.fullname] = count

    @staticmethod
    def items_outgoing(count, item, where):
        if isinstance(count, int):
            print(f'Выдача со склада {count} шт.: {item.type} {item.fullname}. Перемещение в {where}')
            if item.fullname in Warehouse.__office_eq[item.type] and \
                    Warehouse.__office_eq[item.type][item.fullname] >= count:
                Warehouse.__office_eq[item.type][item.fullname] -= count
            else:
                print(f'Ошибка! На складе нет такого количества ({count}) '
                      f'этих устройств: {item.type} {item.fullname}')

    def __str__(self):
        return '\nОстатки по складу\n' + '-' * 30 + '\n' + \
               '\n'.join([f'{eq_type}:\n' + '\n'.join([f'\t{name}: {count} шт.' for name, count in n_type.items()])
                          for eq_type, n_type in Warehouse.__office_eq.items()]) + '\n' + '-' * 30 + '\n'


ware = Warehouse()
ware.items_income(20, Printer('HP', 'LaserJet 100'))
ware.items_income(15, Printer('HP', 'InkJet 100'))
ware.items_income(10, Scanner("HP", "ScanJet 100"))
ware.items_income(5, Copier("Xerox", "Xerox WorkCenter 3335"))
print(ware)

ware.items_outgoing(10, Printer('HP', 'InkJet 100'), 'Office')
print(ware)
