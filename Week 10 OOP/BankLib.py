class BankAccount:
    """Bank account class with balance and interest rate"""

    def __init__(self, balance, AccountNumber):
        """Contruct a bank account. All the bank Account has 5% interest rate"""
        self._balance=balance
        self._rate=0.05
        self._AccountNum = AccountNumber

    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount 
        

    def withdraw(self, amount):
        self._balance -= amount
        
    def calculateInterest(self):
        interest = 0        
        interest = self._balance * self._rate
        return interest
    
    def AddInterest(self, interest):
        self._balance += interest 
        return self._balance
