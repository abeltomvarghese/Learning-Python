#def daysIn(month,year):
#    assert (1 <= month <= 12)
#    assert (year > 1753)
 #   daymonth = ["","31","28","31","30","31","30","31","31","30","31","30","31"]
  #  if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
   #     daymonth[2] = 29
    #    print(year, " is a leap year") 
    #d = daymonth[month]
   # return d


def isLeapYear(Year):
    return (Year % 4 == 0 and Year % 100 !=0) or Year % 400 == 0

def daysIn(month,year):
    assert (1 <= month <= 12)
    assert (year > 1753)
    daymonth = ["","31","28","31","30","31","30","31","31","30","31","30","31"]
    CheckYear = isLeapYear(year)
    if CheckYear == True:
        daymonth[2] = 29
        print(year, " is a leap year")
    d = daymonth[month]
    return d


    


y = int(input("Enter the Year: "))
m = int(input("Enter the Month: "))

days = daysIn(m,y)

print(days, " days in this month ")

