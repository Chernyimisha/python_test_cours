from unittest import TestCase

import pytest

from calculator.Calculator import Calculator


class TestCalculator(TestCase):
    calc = Calculator()

    def test_add(self):

        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, -1) == -2
        assert self.calc.add(0, 0) == 0

    def test_sub(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 5) == -4

    def test_mul(self):
        assert self.calc.multyply(3, 4) == 12

    def test_div(self):
        assert self.calc.divide(8, 0) == 0
        with pytest.raises(ValueError):
            self.calc.divide(1, 0)

