class User:
    bank_name = "Bank of America"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, amount, destination):
        self.account_balance -= amount
        destination.account_balance += amount
        self.display_user_balance()
        destination.display_user_balance()
        return self

david = User("David Bernard", "dpbernard18@gmail.com")
monty = User("Monty Python", "monty@python.com")
steph = User("Steph Rodriguez", "stephrod@gmail.com")
# First user activity
david.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(1500).display_user_balance().transfer_money(500, steph)
# Second user activity
monty.make_deposit(400).make_deposit(900).make_withdrawal(100).make_withdrawal(500).display_user_balance()
# Third user activity
steph.make_deposit(10000).make_withdrawal(300).make_withdrawal(1000).make_withdrawal(600).display_user_balance()
