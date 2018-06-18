import math
PeopleGoing = int(input("Please enter the number of people going on the trip: "))
CoachesNeeded = float(PeopleGoing / 55)
print("You would need ", math.ceil(CoachesNeeded), " coaches")
