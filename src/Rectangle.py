from .Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.name = "Прямоугольник"
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimetr(self):
        return 2 * (self.a + self.b)
