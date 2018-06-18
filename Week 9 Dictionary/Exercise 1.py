import random

digit = ''
for i in range(4):
    digit += str(random.randint(0,9))
print(digit)

pin = input("Please enter your four digit pin:")

hint = ''
for i in range(4):
    if digit[i] == pin[i]:
        hint+='Y'
    elif digit[i] < pin[i]:
        hint += 'L'
    else:
        hint += 'H'

print(hint)
