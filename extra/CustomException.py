class NotEnoughBalance(Exception):
    def __init__(self, amount, balance):
        self.message = f"Insufficient funds. Requested: {
            amount}, Available: {balance}"


class InvalidAmount(Exception):
    def __init__(self, amount):
        self.message = f"Invalid amount: {amount}"


balance = 500


def withdraw(amount):
    global balance
    if amount <= 0:
        raise InvalidAmount(amount)
    if balance < amount:
        raise NotEnoughBalance(amount, balance)
    balance -= amount
    print(f"Rs {amount} deducted. New balance: Rs {balance}")


try:
    withdraw(600)
except Exception as e:
    print(e.message)
except NotEnoughBalance as e:
    print(e.message)
except InvalidAmount as e:
    print(e.message)
