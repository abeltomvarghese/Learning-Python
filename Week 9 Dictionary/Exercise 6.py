def loadDB():
    myFile = open("students.csv", "r")
    students = []
    for line in myFile:
        info = line.split(',')
        s = {}
        s['name'] = info[0]
        s['subject'] = info[1]
        s['modules'] = info[2:]
        students.append(s)
    myFile.close()
    return students


Students = loadDB()
print(Students)
