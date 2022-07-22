from .Figure import Figure
import math


class Circle(Figure):

    def __init__(self, r):
        self.name = "Круг"
        self.r = r

    @property
    def area(self):
        return math.pi * self.r ** 2

    @property
    def perimetr(self):
        return 2 * self.r * math.pi
