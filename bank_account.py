class BankAccount:
    all_inst = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_inst.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.balance = self.balance - amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
            return self

    @classmethod
    def print_inst(cls):
        for i in cls.all_inst:
            i.display_account_info()


user1 = BankAccount(0.01, 100)
user2 = BankAccount(0.01, 0)
user3 = BankAccount(0.01, 111)

user1.deposit(100).deposit(150).deposit(1000).withdraw(
    1000).yield_interest().display_account_info()

user2.deposit(500).deposit(1000).withdraw(200).withdraw(50).withdraw(
    150).withdraw(600).yield_interest().display_account_info()

print("-"*20)
BankAccount.print_inst()
