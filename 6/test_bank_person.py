# Задание №3
# Создайте два класса: Person и Bank. Класс Person должен иметь метод transfer_money,
# который позволяет перевести деньги в Bank. Класс Bank должен иметь метод
# receive_money.
# Напишите тесты, проверяющие корректность взаимодействия этих классов.

import pytest

from Bank import Bank
from Person import Person


@pytest.fixture
def setup():
    bank = Bank()
    person = Person()
    person.add_money(100)
    return bank, person


def test_transfer_money(setup):
    bank, person = setup
    person.transfer_money(bank, 50)
    assert person.money == 50.00, 'test transfer_money failde'
    assert bank.balance == 50, 'test recieve_money failed'
    

# def test_transfer_more_than_balance(setup):
#     bank, person = setup
#     person.transfer_money(bank, 150)
#     assert person.money == 100, 'test transfer more than balance failed'
#     assert bank.balance == 0, 'test receive money failed'
    

def test_transef_negative_amount(setup):
    bank, person = setup
    with pytest.raises(ValueError):
        person.transfer_money(bank, -1)


if __name__ == '__main__':
    pytest.main(['-v'])

    