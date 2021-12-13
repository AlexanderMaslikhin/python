from time import sleep


class TrafficLight:
    __color = [('red', 7), ('yellow', 2), ('green', 10)]

    def running(self, cycles):
        for _ in range(cycles * 3):
            print(f'Горит {TrafficLight.__color[0][0]} в течение {TrafficLight.__color[0][1]} секунд')
            sleep(TrafficLight.__color[0][1])
            print('Переключение')
            self.__switch()

    def __switch(self):
        TrafficLight.__color.append(self.__color.pop(0))


tl = TrafficLight()
tl.running(3)
