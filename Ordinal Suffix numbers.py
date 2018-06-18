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
    else:                       #sometimes it works however 
        suffix = "th"           #most times it just goes straight to else 

print(day, suffix)
        
        
