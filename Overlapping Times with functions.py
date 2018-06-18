def Clash(startA,durA,startB,durB):
    if (startA + durA) > startB:
        return True
    else:
        return False
    
StartA = int(input("Start Hour of A: "))
durA = int(input("Duration of A: "))
StartB = int(input("Start Hour of B: "))
durB = int(input("Duration of B: "))
checkclash = Clash(StartA,durA,StartB,durB)
print(checkclash) 
