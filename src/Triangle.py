from .Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            self.p = (a + b + c) / 2  # вычисляем полумериметр у треугольника
            self.name = "Треугольник"
            self.a, self.b, self.c = a, b, c
        else:
            raise ValueError

    @property
    def area(self):
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    @property
    def perimetr(self):
        return self.a + self.b + self.c


triangle = Triangle(13, 14, 15)
print(triangle.area)
print(triangle.perimetr)
