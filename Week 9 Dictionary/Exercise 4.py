def AddingStudents(students, name, sub, mod):
    info = [] 
    info.append(name)
    info.append(sub)
    modu = []
    for x in range(mod):
        
        moduleName = input("Enter a module name: ")
        modu.append(moduleName)
    
    info.append(modu)

    students.append(info)
    print(students)







addStudent = []
StudentName = input("whats the student name: ")
StudentSub = input("What subject does the student take: ")
StudentMod = int(input("How many modules : "))
AddingStudents(addStudent, StudentName, StudentSub, StudentMod)
