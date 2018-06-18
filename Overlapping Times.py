StartA = int(input("Start Hour of A: "))
EndA = int(input("End Hour of A: "))
StartB = int(input("Start Hour of B: "))
EndB = int(input("End Hour of B: "))
DurationA = StartA + EndA
DurationB = StartB + EndB
if DurationA > DurationB:
    print("Overlapping events")
else:
    print("Events do not overlapp")
    
    


    
