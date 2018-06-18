Pal = input("Enter a palindrome word: ")
validB = False
counter = len(Pal)-1
for p in range(len(Pal)):
    if Pal[p] == Pal[counter]:
        validB = True
    else:
        validB = False
    counter = counter - 1
if validB == True:
    print("Valid Palindrome")
else:
    print("Invalid Palindrome")
    
