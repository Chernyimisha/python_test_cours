from Compar_averages import Compar_averages
from Calc_average_value_list import Calc_average_value_list


class Main:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def print_result_message(self):
        average1 = Calc_average_value_list.calc_average(self.list1)
        average2 = Calc_average_value_list.calc_average(self.list2)
        Compar_averages.compare_averages(average1, average2)


