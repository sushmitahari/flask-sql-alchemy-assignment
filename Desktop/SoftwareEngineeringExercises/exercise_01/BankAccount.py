#Sushmita Hari
class BankAccount:
        def __init__(self, account_name, starting_balance):
            self.account_name = account_name
            self.starting_balance = starting_balance
        def deposit_Money(self, deposit_Account):
            self.starting_balance += deposit_Account
        def withdraw_Money(self, withdraw_Account):
            self.starting_balance -= withdraw_Account
        def get_Balance(self):
            return f"{self.account_name} has a balance of ${self.starting_balance}"