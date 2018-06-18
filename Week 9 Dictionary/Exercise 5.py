def AddStudents(LStudents):
    info = []
    Modules = []
    StudentName = input("Enter the student name: ")
    StudentSub = input("Enter the student subject: ")
    info.append(StudentName)
    info.append(StudentSub)
    NumMod = int(input("Enter number of modules: "))
    for x in range(NumMod):
        ModuleName = input("Enter the Module name: ")
        Modules.append(ModuleName)
    
    info.append(Modules)
    LStudents.append(info)
    return LStudents             
                 



Students = []
CarryOn = "yes"
while CarryOn == "yes":
    Students = AddStudents(Students)
    CarryOn = input("Would you like to enter a new student: ") 
print(Students)
