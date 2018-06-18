def SumOfList(Listofnumbers):
    assert len(Listofnumbers) > 0 
    for x in range(len(Listofnumbers)):
        total = 0 
        total = Listofnumbers[x] + total

    return total


def LowestOfList(Listofnumbers):
    assert len(Listofnumbers) > 0
    lowestNum = Listofnumbers[0]
    for x in range(len(Listofnumbers)):
        if lowestNum > Listofnumbers[x]:
            lowestNum = Listofnumbers[x]
        

    return lowestNum

def HighestOfList(Listofnumbers):
    assert len(Listofnumbers) > 0
    highestNum = Listofnumbers[0]
    for x in range(len(Listofnumbers)):
        if highestNum < Listofnumbers[x]:
            highestNum = Listofnumbers[x]

    return highestNum


def AverageOfList(Listofnumbers):
    assert len(Listofnumbers) > 0
    Divider = len(Listofnumbers)
    for x in range(len(Listofnumbers)):
        total = 0 
        total = Listofnumbers[x] + total

    return Average = total/ Divider 



        
