class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, withdrawal_fee=1):
        super().__init__(owner, balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount):
        total = amount + self.withdrawal_fee
        if total > self.balance:
            print("Not enough money for this withdrawal and its fee.")
        else:
            self.balance -= total


account = CheckingAccount("Sam", 100)
account.deposit(25)
account.withdraw(20)
account.show_balance()
