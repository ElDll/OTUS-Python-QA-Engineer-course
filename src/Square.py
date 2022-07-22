from .Figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.name = "Квадрат"
        self.a = a


    @property
    def area(self):
        return self.a ** 2

    @property
    def perimetr(self):
        return self.a * 4
