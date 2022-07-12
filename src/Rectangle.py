from .Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.name = "Прямоугольник"
        self.area = a * b
        self.perimetr = 2 * (a + b)

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError
