class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in the account.")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate


account = SavingsAccount("Alex", 100)
account.deposit(50)
account.withdraw(20)
account.add_interest()
account.show_balance()
