class Runner(): 
     
    def AddRunner(self, Number, FName, Sname, Time):
        info = []
        NumberAndTime = []
        self._Number = Number 
        self._FName = FName
        self._Sname = Sname
        self._Time = Time
        info.append(self._FName)
        info.append(self._Sname)
        NumberAndTime.append(self._Number)
        NumberAndTime.append(self._Time)
        info.append(NumberAndTime)
        return info
    
    def DisplayRunners(self, RunnerList):
        print(RunnerList)
            





"""choice = input("would you like to enter a runner: ")
runnerFirstN = input("Please enter first name: ") 
runnerLastN = input("Please enter last name: ")
runnerNum = input("Please enter the number: ") 
runnerTime = input("Please enter the time: ")
index = 0 
while choice == "yes": 
    index."""