class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

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
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
            return self


class User:

    def __init__(self, name, email, ):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.02, balance=0), BankAccount(int_rate=0.02, balance=0)]

    def make_deposit(self, amount, a):
        self.account[a].deposit(amount)

        return self

    def make_withdrawal(self, amount, a):
        self.account[a].withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        print(f"Account 1 : ${self.account[0].display_account_info()}")
        print(f"Account 2 : ${self.account[1].display_account_info()}")
        return self

    def transfer_money(self, amount, other_user, a):
        self.account[a].balance -= amount
        other_user.account[a].balance += amount
        return self


user1 = User("Mandy", "firstusers@email.com")
user2 = User("Ludwig", "seconduser@email.com")
user3 = User("Joseph", "noneedemail@ever.huhu")

user1.make_deposit(1000, 0).make_withdrawal(750, 0).make_deposit(1000, 1).make_withdrawal(500, 1).display_user_balance()
user2.make_deposit(100, 0).make_withdrawal(75, 0).make_deposit(100, 1).make_withdrawal(75, 1).display_user_balance()

user1.transfer_money(10, user2, 0).display_user_balance()
user2.transfer_money(10, user1, 1).display_user_balance()


