encryptMessage = str(input("Enter a message to encrypt: "))
offset = int(input("Enter an offset: "))
letter = ""
convert_letter_number = 0
new_number = 0
chartext = ""
ciphertext = ""
for x in range(len(encryptMessage)):
    letter = encryptMessage[x]
    convert_letter_number = ord(letter)
    if convert_letter_number + offset > 122:
        new_number = (convert_letter_number + offset - 97) % 26
        chartext = chr(new_number + 97)
        ciphertext = ciphertext + chartext
    else:
        convert_letter_number += offset
        ciphertext = ciphertext + chr(convert_letter_number)
        

print(ciphertext)

    

             
                