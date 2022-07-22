from src.Circle import Circle
from src.Square import Square
import pytest


def test_correct_calculation_area():
    circle = Circle(5)
    assert 78.5 == round(circle.area, 1), "Неверное вычесление площади"


def test_correct_calculation_perimetr():
    circle = Circle(5)
    assert 31.4 == round(circle.perimetr, 1), "Неверное вычисление периметра"


def test_correct_work_add_area():
    circle = Circle(5)
    square = Square(10)
    assert 178.5 == round(circle.add_area(square), 1), "Неверное сложение площадей двух фигур"


def test_raise_add_area():
    circle = Circle(13)
    with pytest.raises(ValueError):
        circle.add_area("OTUS")
