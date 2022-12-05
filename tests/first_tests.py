import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self,2,2)==4

    def test_multiply_calculator_failed(self):
        assert  self.calc.multiply(self,2,2)==5

    def test_division_calculator_correctly(self):
        assert self.calc.division(self,4,2)==2

    def test_division_subtraction_correctly(self):
        assert self.calc.subtraction(self,6,2)==4

    def test_adding_subtraction_correctly(self):
        assert self.calc.adding(self, 6, 2) == 8

    def test_st_correctly(self):
        assert self.calc.st(self, 6, 2) == 36

    def test_kr_correctly(self):
        assert self.calc.kr(self, 9, 2) == 3