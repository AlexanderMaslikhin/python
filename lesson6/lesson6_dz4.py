from random import randint

class Car:

    def __init__(self, max_speed, color, name):
        self.speed = 0
        self.max_seed = max_speed
        self.name = name
        self.color = color
        self.is_police = False

    def go(self):
        if self.speed == 0:
            self.speed = randint(1, self.max_seed)
            print(f'{self.name} is going')
        else:
            print(f'{self.name} is already going')

    def stop(self):
        if self.speed > 0:
            self.speed = 0
            print(f'{self.name} is stopped')
        else:
            print(f'{self.name} isn\'t going')

    def turn(self, direction):
        if self.speed:
            print(f'{self.name} is turning {direction}')
        else:
            print(f'{self.name} isn\'t going')

    def show_speed(self):
        print(f'Current speed: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name} exceeded the allowed speed 60')


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name} exceeded the allowed speed 40')


class SportCar(Car):

    def __init__(self, name):
        super().__init__(350, 'red', name)


class PoliceCar(Car):

    def __init__(self, max_speed):
        super().__init__(max_speed, 'white_and_blue', 'Police Car')
        self.is_police = True


work_car = WorkCar(80, 'blue', 'Volvo Truck')
work_car.go()
work_car.show_speed()
work_car.turn('right')
work_car.stop()

town_car = TownCar(180, 'yellow', 'Taxi car')
town_car.stop()
town_car.go()
town_car.show_speed()
town_car.turn('left')
town_car.stop()

police_car = PoliceCar(250)
police_car.go()
police_car.show_speed()
print(police_car.is_police)
police_car.stop()
