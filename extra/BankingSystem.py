from abc import ABC, abstractmethod


class BankAccount(ABC):
    name: str
    _acc_num: int
    __bal: int

    def __init__(self, name, acc_num):
        self._acc_num = acc_num
        self.name = name
        self.__bal = 0

    def get_balance(self):
        return self.__bal

    def __set_balance(self, ammount):
        if ammount < 0:
            print("Balance cannot be negative")
        else:
            self.__bal = ammount

    def _update_balance(self, amount):
        self.__set_balance(amount)

    @abstractmethod
    def deposit(self, ammount):
        pass

    @abstractmethod
    def withdraw(self, ammount):
        pass

    @abstractmethod
    def display_balance(self, ammount):
        pass


class SavingsAccount(BankAccount):
    MIN_BALANCE = 500

    def __init__(self, name, acc_num):
        super().__init__(name, acc_num)
        self._update_balance(self.MIN_BALANCE)

    def deposit(self, ammount):
        self._update_balance(self.get_balance()+ammount)
        print(f"Deposit of {ammount} Successfull")
        self.display_balance()

    def withdraw(self, ammount):
        if ammount > self.get_balance():
            print("Insufficient Balance")
        else:
            self._update_balance(self.get_balance()-ammount)
            print(f"Withdraw  of {ammount} Successfull")
            self.display_balance()

    def display_balance(self):
        print("Current Balance: ", self.get_balance())


class CurrentAccount(SavingsAccount):
    def __init__(self, name, acc_num, bal):
        super().__init__(name, acc_num)
        self._update_balance(bal)

    def deposit(self, ammount):
        self._update_balance(self.get_balance()+ammount)
        print(f"Deposit of {ammount} Successfull")
        self.display_balance()

    def withdraw(self, ammount):
        if ammount > self.get_balance():
            print("Insufficient Balance")
        elif ammount > 10000:
            print("Cannot Withdraw more than 10,000")
        else:
            self._update_balance(self.get_balance()-ammount)
            print(f"Withdraw  of {ammount} Successfull")
            self.display_balance()

    def display_balance(self):
        print("Current Balance: ", self.get_balance())


class FixedDepositAccount(BankAccount):
    intrest_rate: int

    def __init__(self, name, acc_num, fixed_ammount, intrest_rate):
        super().__init__(name, acc_num)
        self._update_balance(fixed_ammount)
        self.intrest_rate = intrest_rate

    def deposit(self, ammount):
        self._update_balance(self.get_balance()+ammount)
        print(f"Deposit of {ammount} Successfull")
        self.display_balance()

    def display_balance(self):
        print("Current Balance: ", self.get_balance())
        print("Next Year", ((self.get_balance() *
              self.intrest_rate)/100) + self.get_balance())

    def withdraw(self, ammount):
        print(f"Cannot Withdraw {ammount} Right Now")
