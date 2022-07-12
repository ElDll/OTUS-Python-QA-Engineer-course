from .Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            p = (a + b + c) / 2  # вычисляем полумериметр у треугольника
            self.name = "Треугольник"
            self.area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            self.perimetr = a + b + c
        else:
            raise ValueError

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError
