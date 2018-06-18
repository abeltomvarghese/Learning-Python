lojban=["no", "pa", "re", "ci", "vo", "mu", "xa", "ze","bi","so" ]
date = input("Enter the date: ")
outputstring = ""
for j in range(len(str(date))):
    specificnumber = int(date[j])
    outputstring = outputstring + lojban[specificnumber]
print(outputstring)





