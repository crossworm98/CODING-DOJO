class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        self.balance += self.balance * 0.01
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
        self.account = {
            "checking": BankAccount(0.01,0),
            "savings": BankAccount(0.01,0)
        }
    def make_deposit(self, amount):
        self.account['checking'].balance += amount
        return self
    def make_deposit_savings(self, amount):
        self.account['savings'].balance += amount
        return self
    def make_withdraw(self, amount):
        self.account['checking'].balance -= amount
        return self
    def make_withdraw_savings(self, amount):
        self.account['savings'].balance -= amount
        return self
    def display_user_balance(self):
        self.account["checking"].yield_interest()
        print(f'Checkings Account: {self.account["checking"].display_account_info()}')
        print(f'Savings Account: {self.account["savings"].display_account_info()}')
        return self


billy = User("Billy Bob").display_user_balance().make_deposit(100).make_withdraw(10).display_user_balance()
bob = BankAccount("bob")
joe = BankAccount("joe")
bob.deposit(100).deposit(32).deposit(74).withdraw(27).yield_interest().display_account_info()
joe.deposit(250).deposit(1253).withdraw(120).withdraw(320).withdraw(40).withdraw(250).yield_interest().display_account_info()
