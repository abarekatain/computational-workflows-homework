# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            raise InsufficientAmount()

    def add_cash(self, amount):
        self.balance = self.balance + amount
