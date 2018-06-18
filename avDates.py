def isLeapYear(Year):
    return (Year % 4 == 0 and Year % 100 !=0) or Year % 400 == 0

#comment
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


def ValidDates(d,m,y): 
    ValidDay = int(daysIn(m,y))
    if 1 <= d <= ValidDay: 
        print(d, "/", m,"/",y," IS a valid date")
         
    elif d > ValidDay or d < 1: 
        print(d, "/", m,"/",y," is NOT a valid date")
