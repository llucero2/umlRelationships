from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

card = CreditCardProcessor()
card.pay(50)  