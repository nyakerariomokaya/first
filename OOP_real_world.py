class CoopAccount():

    def __init__(self):
        pass

    def withdraw():
        pass
    def deposit():
        pass

class CoopSavings(CoopAccount):

    def __init__(self):
        self.balance = 800

    def deposit(self, amount_deposited):
        if (amount_deposited < 0):
            return "Invalid deposit amount"
        else:
            self.balance +=amount_deposited
            return self.balance

    def withdraw(self, amount_withdrawn):
       
        if ((self.balance - amount_withdrawn) > 0) and ((self.balance - amount_withdrawn) < 500):
            return "Cannot withdraw beyond the minimum account balance"
        elif (self.balance - amount_withdrawn) < 0:
            return "Insufficient funds"
        elif amount_withdrawn < 0:
            return "Invalid withdraw amount"
        else:
            self.balance -= amount_withdrawn
            return self.balance 
class CoopCurrentAccount(CoopAccount):

    def __init__(self):
        self.balance = 0


    def deposit(self, amount):
        if amount < 0:
            return "Invalid  amount"
        else:
            self.balance += amount
            return self.balance


    def withdraw(self, amount):
        if amount < 0:
            return "Invalid amount"
        elif self.balance < amount:
            return "You dont have enough funds to withdraw that amount"
        else:
            self.balance -= amount
            return self.balance

