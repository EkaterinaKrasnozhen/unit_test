from credit_card import CreditCard

class PaymentForm():
    def __init__(self, credit_card: CreditCard) -> None:
        self._credit_card = credit_card
        
    @property
    def credit_card(self):
        return self._credit_card
    
    def pay(self, amount: float) -> None:
        self._credit_card.charge(amount)