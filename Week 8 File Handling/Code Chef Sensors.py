import time
start_time = time.clock()
def Calculation(HowMuch,AllList): 
    i = 0
    Sync = False
    AllList.replace("\n","")
    NewList = AllList.split()
    while Sync == False: 
        i+=1
        for L in range(int(HowMuch)):
            quotient = NewList[L]
            sensor = int(i) // int(quotient)
            for K in range(int(HowMuch)-1):
                if sensor == int(NewList[K+1]):
                    Sync = True
    
    
    
    wow = CheckSameElements(HowMuch,NewList,i)
    if int(wow) < i:
        print(wow)
    else:
        print(i)

def CheckSameElements(HowM,Newlist,i):
    
    for x in range(int(HowM)):
        counter = 0
        SingleElement = Newlist[x]
        for Q in range(int(HowM)):
            if SingleElement == Newlist[Q]:
                counter +=1
                if counter > 1:
                    return SingleElement
                
    
    return i
    
    #print(i)
  
    

file = open("Micro.txt","r") 
ControllersNum = file.readline()

for x in range(int(ControllersNum)):
    HowMany = file.readline()
    list = file.readline()
    Calculation(HowMany.replace("\n",""),list.replace("\n",""))

print(time.clock() - start_time, "seconds")