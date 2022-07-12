import math
from .Figure import Figure


class Circle:

    def __init__(self, r):
        self.name = "Круг"
        self.area = math.pi * r ** 2
        self.perimetr = 2 * r * math.pi

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError
