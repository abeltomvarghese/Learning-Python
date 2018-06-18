file = open("Example1.txt")     
list= file.readlines()                          #First Method
print(list)

file.seek(0)                                    #Second Method
for line in file:
    print(line)

file.seek(0)
read_whole_file= file.read()                    #Third Method
print(read_whole_file)

file.seek(0)                                    #Forth Method
read_the_line = file.readline()

print(read_the_line)





