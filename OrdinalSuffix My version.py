day = int(input("day? "))
suffix = ""

if day == 11 or day == 12 or day == 13:
    suffix = "th"
else:
    if day % 10 == 1:                   
        suffix = "st"
    if day % 10 == 2:
        suffix = "nd"
    if day % 10 == 3:
        suffix = "rd"
    elif (day % 10 != 1) and (day % 10 != 2) and (day % 10 != 3):   
        suffix = "th"
print(day, suffix)
