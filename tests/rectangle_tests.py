from src.Rectangle import Rectangle
from src.Square import Square
import pytest


def test_correct_calculation_area():
    rectangle = Rectangle(13, 14)
    assert 182 == rectangle.area, "Неверное вычесление площади"


def test_correct_calculation_perimetr():
    rectangle = Rectangle(13, 14)
    assert 54 == rectangle.perimetr, "Неверное вычисление периметра"


def test_correct_work_add_area():
    rectangle = Rectangle(13, 14)
    square = Square(10)
    assert 282 == rectangle.add_area(square), "Неверное сложение площадей двух фигур"


def test_raise_add_area():
    rectangle = Rectangle(13, 14)
    with pytest.raises(ValueError):
        rectangle.add_area("OTUS")
