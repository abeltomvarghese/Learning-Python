import re
ValidPassword = False
Vlowercase = False
Vuppercase = False
VDigit = False
lowercaseCounter = 0 
uppercaseCounter = 0 
digitCounter = 0 
wrongOutput = str("Invalid Password")
validOutput = str("valid Password")
while ValidPassword == False or Vlowercase == False or Vuppercase == False or VDigit == False:
    ValidPassword = True
    Vlowercase = False
    Vuppercase = False
    VDigit = False
    lowercaseCounter = 0 
    uppercaseCounter = 0 
    digitCounter = 0     
    passwordAttempt = str(input("Please enter a password: "))
    if len(passwordAttempt) <= 6: 
        print(wrongOutput) 
        ValidPassword = False
    elif len(passwordAttempt) > 15:
        print(wrongOutput) 
        ValidPassword = False
        
    for i in range(len(passwordAttempt) -1):
        if passwordAttempt[i] == passwordAttempt[i + 1] :
            print(wrongOutput + ": Password must not contain two ")
            print("adjacent characters that are the same")
            ValidPassword = False           
        elif "a" <= passwordAttempt[i] <= "z":
            lowercaseCounter += 1 
            Vlowercase = True            
        elif "A" <= passwordAttempt[i] <= "Z":
            uppercaseCounter += 1 
            Vuppercase = True
            #ValidPassword = True            
        elif "0" <= passwordAttempt[i] <= "9":
            digitCounter += 1
            VDigit = True
            #ValidPassword = True           
        else:
            print(wrongOutput + ": Passwords must not contain special characters")
            ValidPassword = False       
    if digitCounter == 0 :
        print(wrongOutput + " Passwords must contain numeric characters")
        VDigit = False
        
    elif lowercaseCounter == 0:
        print(wrongOutput + " Passwords must contain lowercase characters")
        Vlowercase = False
    elif uppercaseCounter == 0:
        print(wrongOutput + " Passwords must contain uppercase characters")
        Vuppercase = False
    elif Vuppercase == True and Vlowercase == True and VDigit == True and ValidPassword == True:
        ValidPassword = True
        print(validOutput)
        
