class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.image - other.image)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.image * other.image,
                       self.real * other.image + self.image * other.real)

    def __str__(self):
        return f'{self.real}+{self.image}i'


a = Complex(2, 1)
b = Complex(3, 4)

print(a + b, a * b, b - a)