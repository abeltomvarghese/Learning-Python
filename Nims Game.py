import random 
def playNovice(marbles):
    NewMarbles = random.randint(1,(marbles//2))
    
    return NewMarbles

def userPlay(marbles):
    getmarbles = int(input("how many marbles? "))
    while getmarbles > marbles//2:
        print("ERROR: The number of marbles selected is above half") 
        getmarbles = int(input("how many marbles? "))

    return  getmarbles


def playExpert(marbles):
    i=1
    valNum=False
    while valNum == False:
            NewMarbles = ((2**i)-1)
            if marbles - NewMarbles < marbles//2:
                valNum = True
            i+=1
    """
        NewMarbles = random.randint(1,(marbles//2))
        for x in range(1,6):
            if NewMarbles != ((2**x)-1):
                valNum = False
            elif NewMarbles == ((2**x)-1):
                valNum = True
                """
                
    return marbles - NewMarbles






marbles = 100

FirstUser = input("Who starts the game? (C/M): ")
GameMode = input("What mode should the game be? (N/E): ")

print("Number of marbles: ", marbles)
while marbles > 1:
    
    """
    if FirstUser = "M":
        marbles = userPlay(marbles)
    elif GameMode = "N":
        marbles = playNovice(marbles)
    """
    if FirstUser == "M" :
        marbles -= userPlay(marbles)
        print("Number of marbles: ", marbles)
       
    elif FirstUser == "C" and GameMode == "N":
        marbles -= playNovice(marbles)
        print("Number of marbles: ", marbles)
    else :
         
        marbles -= playExpert(marbles)
        
        print("Number of marbles: ", marbles)
        
    if FirstUser == "M":
        FirstUser = "C"
    else:
        FirstUser = "M"

if FirstUser == "M":
    FirstUser = "C"
    print(FirstUser + " has won")
elif FirstUser == "C":
    FirstUser = "M"
    print(FirstUser + " has won")
    
 
