# def isLeapYear(year):
    #if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
       # leap = "is a leap year"
    #else:
        #leap = "is not a leap year"
    #return leap
import sys 
def isLeapYear(Year):
    return (Year % 4 == 0 and Year % 100 !=0) or Year % 400 == 0

Year = int(input("Enter a year: "))
aYear = isLeapYear(Year)
print(Year, aYear)
sys.stdin.readline()
