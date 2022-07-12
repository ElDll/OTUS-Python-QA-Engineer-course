from src.Triangle import Triangle
from src.Square import Square
import pytest


def test_create_incorrect_triangle():
    with pytest.raises(ValueError):
        Triangle(5, 5, 15)


def test_correct_calculation_area():
    triangle = Triangle(13, 14, 15)
    assert 84 == triangle.area, "Неверное вычесление площади"


def test_correct_calculation_perimetr():
    triangle = Triangle(13, 14, 15)
    assert 42 == triangle.perimetr, "Неверное вычисление периметра"


def test_correct_work_add_area():
    triangle = Triangle(13, 14, 15)
    square = Square(10)
    assert 184 == triangle.add_area(square), "Неверное сложение площадей двух фигур"


def test_raise_add_area():
    triangle = Triangle(13, 14, 15)
    with pytest.raises(ValueError):
        triangle.add_area("OTUS")


