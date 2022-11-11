alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input("message for decrypting: ").upper()
number = int(input('key of decrypring: '))
text = ''
for letter in message:
    index = alphabet.find(letter)
    newIndex = index + number
    if letter in alphabet:
        text += alphabet[newIndex]
    else:
        text += letter
print(text)