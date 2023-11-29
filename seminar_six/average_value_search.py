# Задание №2
# Модифицируйте функцию find_average так, чтобы она вызывала исключение TypeError, если
# ей передается не список.
# Напишите тест, который проверяет вызов этого исключения


import pytest


def find_average(numbers: list) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


n = []
print(find_average(n))


def test_find_average():
    assert find_average([1, 2, 3]) == 2
    assert find_average([]) == 0
    assert find_average([5]) == 5


def test_find_average_type():
    with pytest.raises(TypeError):
        find_average('foo')
