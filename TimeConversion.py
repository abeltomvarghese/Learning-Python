secondToConvert = int(input("Please Enter the seconds: "))
minute = secondToConvert / 60   #divide to get the total minutes 
seconds = secondToConvert %60   #mod to get the left over seconds.

hour = minute / 60      #get how many hours in total 
minutes = minute % 60    #mod to get left over minutes from the biggest full hour

days = hour / 24         #get the days in total 
hours = hour % 24        #mod to get the left over hours since the biggest full day 

outputdays = int(days)
outputhours = int(hours)
outputminutes = int(minutes)
outputseconds = int(seconds)

print("%dd %dH %dm  %ds" % (outputdays,outputhours,outputminutes,outputseconds))


