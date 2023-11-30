class Calc_average_value_list:
    @staticmethod
    def calc_average(numbers: list) -> float:
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
