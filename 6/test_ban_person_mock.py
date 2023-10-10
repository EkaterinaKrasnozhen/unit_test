# Задание №4
# В предыдущем задании используйте unittest.mock для создания мок-объекта Bank.
# Напишите тест, в котором вы проверите, вызывается ли метод receive_money с правильным
# аргументом.
import pytest
from unittest.mock import Mock
from Bank import Bank
from Person import Person


@pytest.fixture
def setup():
    bank = Mock()
    person = Person()
    person.add_money(100)
    return bank, person


def test_bank_mock(setup):
    bank, person = setup
    person.transfer_money(bank, 100)
    bank.receive_money.assert_called_with(100)
    
    
if __name__ == '__main__':
    pytest.main(['-v'])
    
