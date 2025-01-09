from BankingSystem import CurrentAccount, SavingsAccount, FixedDepositAccount


class test:
    name = "test"

    def hello(self):
        return "This"


t = test()
print(t.name)
print(t.hello())


# if __name__ == "__main__":
# sa1 = SavingsAccount("Jash", 1234567890)
# sa1.display_balance()
# sa1.deposit(500)
# sa1.withdraw(1001)
# sa1.withdraw(1000)
# sa1.deposit(5000)

# ca1 = CurrentAccount("Jash",1234567890,5000)
# ca1.display_balance()
# ca1.deposit(10000)
# ca1.withdraw(12000)
# ca1.withdraw(8000)

# fd1 = FixedDepositAccount("Jash", 1234567890, 50000, 12)
# fd1.display_balance()
# fd1.deposit(ammount=30000)
