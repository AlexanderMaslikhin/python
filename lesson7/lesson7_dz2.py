from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_outgo(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cloth_outgo(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cloth_outgo(self):
        return self.height * 2 + 0.3


coat = Coat("Пальто", 10)
print(coat.cloth_outgo)
costume = Costume("Тройка", 5)
print(costume.cloth_outgo)
