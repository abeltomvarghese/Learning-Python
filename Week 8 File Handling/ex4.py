file = open("Example1.txt")
line1 = file.readline()
line2 = file.readline()
list1 = line1.split()
list2 = line2.split()

if len(list1) < len(list2):
    Length = len(list1)
else:
    Length = len(list2)

for i in range(Length):
    print(list1[i] + " " + list2[i])
    
