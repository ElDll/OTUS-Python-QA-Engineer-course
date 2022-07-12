from .Figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.name = "Квадрат"
        self.area = a ** 2
        self.perimetr = a * 4

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError
