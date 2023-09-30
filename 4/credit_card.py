# Задание №2
# Используя библиотеку Mockito, напишите модульные тесты для проверки функциональности формы
# оплаты на сайте. Вместо реальной кредитной карты используйте мок-объект.
# 1. Создайте класс `CreditCard` с методами `getCardNumber()`, `getCardHolder()`,
# `getExpiryDate()`, `getCvv()`, `charge(double amount)`.
# 2. Создайте класс `PaymentForm` с методом `pay(double amount)`.
# 3. В тестовом классе, создайте мок-объект для класса `CreditCard`.
# 4. Определите поведение мок-объекта с помощью метода `when()`.
# 5. Создайте объект класса `PaymentForm`, передайте ему мок-объект в качестве аргумента.
# 6. Вызовите метод `pay()` и убедитесь, что мок-объект вызывает метод `charge()`

class CreditCard:
    def __init__(self, card_number: str, card_holder: str, expirity_date: str, cvc: str) -> None:
        self._card_number = card_number
        self._card_holder = card_holder
        self._expirity_date =  expirity_date
        self._cvc = cvc
    
    @property    
    def card_number(self):
        return self._card_number
    
    @property
    def card_holder(self):
        return self._card_holder
    
    @property
    def expirity_date(self):
        return self._expirity_date
    
    @property
    def cvc(self):
        return self._cvc
    
    def charge(self, amount: float):
        print(f'Оплата с карты {self.card_number} на сумму {amount}.')
    