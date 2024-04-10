alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(planText, shiftNum):
    newWord = ''
    for position in planText:
        letter = alphabet.index(position)
        newPosition = letter + shiftNum
        newLetter = alphabet[newPosition]
        newWord += newLetter
    print(newWord)


def decrypt(cipherText, shiftNum):
    planText = ''
    for position in cipherText:
        letter = alphabet.index(position)
        newPosition = letter - shiftNum
        newLetter = alphabet[newPosition]
        planText += newLetter
    print(planText)


if direction == 'encode':
    encrypt(planText=text, shiftNum=shift)
elif direction == 'decode':
    decrypt(cipherText=text, shiftNum=shift)
else:
    print('Please enter appropriate word')
