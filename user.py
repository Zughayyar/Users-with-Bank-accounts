########################
#### Anas Zughayyar ####
########################
########  User  ########
########################

from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    
    def display_account_info(self):
        print(f"Accounts Balances of - {self.name} - ")
        print("Balance (USD):", self.account.usd)
        print("Balance (NIS):", self.account.ils)
        