def UserDetails():
    ValidInput = 0
    Username = input("Please enter your name: ")
    try: 
        UserAge = int(input("Please enter your age: ")) 
    except ValueError: 
        print("Sorry your age has to be numeric characters") 
    
    UserCourse = input("Please enter your course: ")
    UserTown = input("Please enter your home town: ") 
    WriteThis(Username,UserAge,UserCourse,UserTown) 
    

def WriteThis(name,age,course,town): 
    try: 
        file = open("Details.txt","a")
        file.write(name + " ")
        file.write(str(age) + " ")
        file.write(course + " ")
        file.write(town)
        file.write("\n") 
    except IOError as err:
        print("Error writing to file: ",err)
    finally:
        file.close()
        

TakeAnotherInput = "yes"
while TakeAnotherInput =="yes":
    UserDetails()
    TakeAnotherInput = input("Would you like to enter another persons Details? ") 

ReadingTheFile = open("Details.txt") 
for OneLine in ReadingTheFile: 
    print(OneLine, end="")