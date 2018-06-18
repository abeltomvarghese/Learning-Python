import math

def distanceBetween(x1,x2,x3,x4):
    distance = 0
    distance = math.sqrt(((x1 - x2)**2) + ((y1-y2)**2))
    return distance

x1 = int(input("Enter first x coordinate: "))
x2 = int(input("Enter second x coordinate: "))
y1 = int(input("Enter first y coordinate: "))
y2 = int(input("Enter second y coordinate: "))
distance = distanceBetween(x1,x2,y1,y2)
print(distance)

