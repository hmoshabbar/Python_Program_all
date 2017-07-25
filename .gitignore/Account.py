# First i am defining a class Account
class BankAccount(object):
    def __init__(self):
       self.balance=5000

    def  Deposit(self,amount):
        self.balance +=amount     #self.balance + amount=amount  its same we can write self.balance +=amount.
        return self.balance

    def withdraw(self,amount):
        if ((self.balance-amount)<0):
            return "You Entered money  is not Vaild"
        else:
            self.balance -=amount
            return self.balance
        

    def balance(self):
        return self.balance

    def transfer(self,amount):
        if ((self.balance-amount)<0):
            return 'You Cant Transfer Money Your balance low'
        else:
            self.balance -=amount
            return "Transaction is sucessfull Now Your Main Balance:" ,self.balance
            
            
            
        
        
