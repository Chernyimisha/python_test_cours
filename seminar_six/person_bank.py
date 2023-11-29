class Person:
    def __init__(self, balance):
        self.balance = balance

    def transfer_money(self, bank, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError ("Недостаточно средств")
        self.balance -= amount
        bank.receive_money(amount)


class Bank:
    def __init__(self):
        self.balance = 0

    def receive_money(self, amount):
        self.balance += amount


def test_person_bank():
    person = Person(1000)
    bank = Bank()
    person.transfer_money(bank, 500)
    assert person.balance == 500
    assert bank.balance == 500






