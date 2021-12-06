class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def material_count(self, material_per_square_meter, thickness):
        return (self._length * self._width * material_per_square_meter * thickness) / 1000


road = Road(20, 5000)
print(road.material_count(25, 5))
