def printStudent(studentList):
    for info in range(len(studentList)):
        if info < 2:
            print(studentList[info])
        else:
            for mod in studentList[2]:
                print(mod)











Student = ["Abel Tom Varghese", "Computer Science",["u08007","u08008","u08010"]]
printStudent(Student) 
