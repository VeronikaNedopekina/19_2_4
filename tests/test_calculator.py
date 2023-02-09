import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 4) == 1

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 6) == 18

    def test_division_success(self):
        assert self.calc.division(self, 8, 2) == 4
