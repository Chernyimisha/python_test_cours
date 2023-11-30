import pytest
import io
import sys
from Compar_averages import Compar_averages
from Calc_average_value_list import Calc_average_value_list
from Main import Main


class Test_compar_averages_value_list(unittest.TestCase):

    def test_calc_average(self):
        assert Calc_average_value_list.calc_average([]) == 0
        assert Calc_average_value_list.calc_average([10]) == 10
        assert Calc_average_value_list.calc_average([1, 2, 3]) == 2

    def test_compar_averages1(self):
        captured = io.StringIO()
        sys.stdout = captured
        Compar_averages.compare_averages(12, 6)
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Первый список имеет большее среднее значение\n"

    def test_compar_averages2(self):
        captured = io.StringIO()
        sys.stdout = captured
        Compar_averages.compare_averages(1, 6)
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Второй список имеет большее среднее значение\n"

    def test_compar_averages3(self):
        captured = io.StringIO()
        sys.stdout = captured
        Compar_averages.compare_averages(1, 1)
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Средние значения равны\n"

    def test_main_compar_averages1(self):
        test = Main([5, 6, 12], [1, 2, 3])
        captured = io.StringIO()
        sys.stdout = captured
        test.print_result_message()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Первый список имеет большее среднее значение\n"

    def test_main_compar_averages2(self):
        test = Main([], [1, 2, 3])
        captured = io.StringIO()
        sys.stdout = captured
        test.print_result_message()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Второй список имеет большее среднее значение\n"

    def test_main_compar_averages3(self):
        test = Main([], [])
        captured = io.StringIO()
        sys.stdout = captured
        test.print_result_message()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Средние значения равны\n"

    def test_main_compar_type(self):
        with pytest.raises(TypeError):
            main = Main(["5"], [5, 3, 7])
            main.print_result_message()

