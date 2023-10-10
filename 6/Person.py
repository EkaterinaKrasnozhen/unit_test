from Bank import Bank

class Person:
    def __init__(self):
        self.money = 0.00
        
    def add_money(self, sum: float) -> None:
        self.money += sum
        
    def transfer_money(self, bank: Bank, amount: float) -> None:
        if self.money >= amount > 0:
            bank.receive_money(amount)
            self.money -= amount
        else:
            raise ValueError('not valid amount')