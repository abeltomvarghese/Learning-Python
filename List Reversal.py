s= ["a","b","c","d"]
print("The list is ", s)
i = 0
while i < len(s)/2: 
    t = s[len(s)-1-i]
    s[len(s)-1-i] = s[i]
    
    s[i] = t
    
    i = i + 1
print("The reversed list is ",s)
