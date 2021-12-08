class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'{self.name}, {self.account_balance}')
        return self


billy = User("Billy Bob")
billy.make_deposit(1000).make_withdraw(100).display_user_balance()
# print(billy.account_balance)