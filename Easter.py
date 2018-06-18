Year = int(input("Enter the year: "))
a = Year%19
b = Year//100
c = Year%100
d = b//4
e = b%4
f = (b+8)//25
g = (b-f+1)//3
h = (((((19*a)+b)-d)-g)+15)%30 
i = c//4
k = c%4
l = (32+(2*e)+(2*i)-h-k)%7
m = (a+(11*h)+(22*l))//451
n = (h+l-(7*m)+114)//31
p = (h+l-(7*m)+114)%31
print(p+1,n,Year)

