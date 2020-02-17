# This is a bank with two types of accounts: Current and Savings. You can create an account and then deposit, 
# withdraw and show statement the account. Printing the account name will present information of the account owner and the balance.

class Account:
    def __init__(self, name, balance, min_balance): # this is a constructor method/function
        self.name = name # states within the constructor method
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount # this is basically the same as "self.balance = self.balance + amount"

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance: # "If your account balance minus the amount you want to withdraw is larger than or equal to your minimum balance:"
            self.balance -= amount # again, this is "self.balance = self.balance - amount"
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))

class Current(Account): # Current child of Account
    def __init__(self, name, balance): # these are the parameter someone has to enter to create their current account.
        super().__init__(name, balance, min_balance = -1000) # give an overdraft of £-1000

    def __str__(self):
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance) # If you print(self) now, it will output a nice presentation of the account and balance.

class Savings(Account): # Savings child of Account
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0) # Can't overdraft the savings account. No can do!

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance) 
