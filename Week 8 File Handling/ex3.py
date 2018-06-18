file = open("Example1.txt")
first_line = file.readline()
file.seek(28)
read_second_line = file.read()
print(read_second_line)

print(first_line)

