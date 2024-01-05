

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plainText, shiftAmount):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is:{cipherText}")
    
def decrypt(cipherText, shiftAmount):
    plainText = ""
    for letter in cipherText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount
        plainText += alphabet[newPosition]
    print(f"The decoded text is:{plainText}")
    
    
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)