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
    
myAccount = BankAccount(100,1)
myAccount.deposit(50)
myAccount.withdraw(25)
myOtherAccount = BankAccount(1000,2)
newinterest = myOtherAccount.calculateInterest()
myAccount.AddInterest(newinterest)

print("Account Number: ", myAccount._AccountNum)
print("Balance of my account is: ", myAccount.getBalance())
print("\n")
print("Account Number: ", myOtherAccount._AccountNum)
print("Balance of my account is: ", myOtherAccount.getBalance())
