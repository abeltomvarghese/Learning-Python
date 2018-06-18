pwd = input("Enter your password: ")
i = 2
k= 0 
duplicates = False
while i <= len(pwd) and duplicates == False:
    k = 1 
    while 2*k <= i and duplicates == False:
        
        duplicates = pwd[i-2*k:i-k] == pwd[i-k:i]
        k+= 1 
    
    
    i+= 1 

if duplicates: 
    print("Not acceptable")
else:
    print("Acceptable")