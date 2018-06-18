import BankLib
mySavings = BankLib.BankAccount(100,1)
UserInput = "yes"
while UserInput == "yes":
    print("Please select from the following options: \n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Get Interest")
    print("\n")
    
    options = int(input("Option: "))
    if options > 4 or options < 1:
        print("ERROR! Incorrect option")
    if options == 1: 
        depositamount = int(input("Please enter the amount: "))
        mySavings.deposit(depositamount)
    elif options == 2: 
        withdrawamount = int(input("Please enter the amount: "))
        balance = mySavings.getBalance()
        if withdrawamount > balance:
            print("Cannot withdraw that amount of money!")
        else:
            mySavings.withdraw(withdrawamount)
    elif options == 3: 
        balance = mySavings.getBalance()
        print("Remaining amount: ", balance) 
    elif options == 4:
        NewInterest = mySavings.calculateInterest()
        print("Interest: ",NewInterest)
        mySavings.AddInterest(NewInterest)
        
    UserInput = input("Would you like to continue? ")     
    
        
    