from src.Square import Square
from src.Triangle import Triangle
import pytest


def test_correct_calculation_area():
    square = Square(13)
    assert 169 == square.area, "Неверное вычесление площади"


def test_correct_calculation_perimetr():
    square = Square(13)
    assert 52 == square.perimetr, "Неверное вычисление периметра"


def test_correct_work_add_area():
    square = Square(13)
    triangle = Triangle(13, 14, 15)
    assert 253 == square.add_area(triangle), "Неверное сложение площадей двух фигур"


def test_raise_add_area():
    square = Square(13)
    with pytest.raises(ValueError):
        square.add_area("OTUS")
