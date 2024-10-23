########################
#### Anas Zughayyar ####
########################
##### Bank Account #####
########################

class BankAccount:
    def __init__(self, int_rate = 0, balance_USD = 0 , balance_ILS = 0):
        self.int_rate = int_rate
        self.usd = balance_USD
        self.ils = balance_ILS

    
    def deposit(self, amount,account_type ):
        if account_type is "usd":
            self.usd += amount
        if account_type is "ils":
            self.ils += amount
        return self
    
    def withdraw(self, amount, account_type):
        if account_type is "usd":
            if self.usd < amount:
                print("Insufficient funds: Charging $5 fee")
                self.usd -= 5
            else:
                self.usd -= amount
        if account_type is "ils":
            if self.ils < amount:
                print("Insufficient funds: Charging NIS15 fee")
                self.ils -= 15
            else:
                self.ils -= amount
        return self
        
    def yield_interest(self):
        if self.usd > 0:
            self.usd += self.int_rate * self.usd
        if self.ils > 0:
            self.ils += self.int_rate * self.ils
        return self

