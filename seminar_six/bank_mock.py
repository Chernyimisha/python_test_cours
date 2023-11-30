# Задание №4
# В предыдущем задании используйте unittest.mock для создания мок-объекта Bank.
# Напишите тест, в котором вы проверите, вызывается ли метод receive_money с правильным
# аргументом.
import unittest.mock


class Person:
    def __init__(self, balance):
        self.balance = balance

    def transfer_money(self, bank, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        bank.receive_money(amount)


class Bank:
    def __init__(self):
        self.balance = 0

    def receive_money(self, amount):
        self.balance += amount


def test_transfer_with_mock():
    bank = unittest.mock.Mock()
    person = Person(1000)
    person.transfer_money(bank, 500)
    bank.receive_money.assert_called_with(480)

# C:\Users\chern\AppData\Local\Programs\Python\Python39\Scripts\pip - путь к pip и другим командам python на ноуте
# C:\Users\chern\AppData\Local\Programs\Python\Python39\Scripts\coverage run -m pytest .\seminar_six\bank_mock.py - создание отчета о покрытии
# C:\Users\chern\AppData\Local\Programs\Python\Python39\Scripts\coverage report -m  - читаем отчет о покрытии
