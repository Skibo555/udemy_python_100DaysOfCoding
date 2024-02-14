alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# For Encryption
def encrypt(text, shift):
    cipher_text = ''
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The encoded text is {}".format(cipher_text))


# For decryption
def decrypt(text, shift):
    cipher_text = ''
    for i in text:
        position = alphabet.index(i)
        new_position = position - shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The decoded text is {}".format(cipher_text))

def caeser():
    if direction == 'encode':
        encrypt(text=text, shift=shift)
    if direction == 'decode':
        decrypt(text=text, shift=shift)

caeser()
wants_more = input("Do you want to perform more tasks? Type yes or no. \n")
wants_more.lower()
if wants_more == "yes":
    caeser()
if wants_more == "no":
    print("Thank you for BANKING WITH US.")