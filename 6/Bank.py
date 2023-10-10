class Bank:
    def __init__(self):
        self.balance = 0.00
        
    def receive_money(self, amount: float) -> None:
        self.balance += amount