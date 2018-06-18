monthdays = ["","31","28","31","30","31","30","31","31","30","31","30","31"]
NumofMonth = int(input("Enter the month num: "))
Year = int(input("Enter the year: "))
if Year % 4 == 0 and (Year % 100!= 0) or Year % 400 == 0:
    monthdays[2] = 29
    print("This year is a leap year") 
outputString = monthdays[NumofMonth]

print("this month has " + str(outputString) + " days, in the year " + str(Year))


                 
