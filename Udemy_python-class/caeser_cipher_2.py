from cipher_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ''
    if direction == "encode":
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += char
        print("The encoded text is {}".format(end_text))
    end_text = ""
    if direction == "decode":
        for i in text:
            if i in alphabet:
                position = alphabet.index(i)
                new_position = position - shift
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += i
        print("The encoded text is {}".format(end_text))

wants_to_contiune = True
while wants_to_contiune:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text=text, shift=shift, direction=direction)
    contiune = input("Do you still want to decode or encode anything? Type 'yes' to continue and 'no' to put a stop to the program.\n").lower()
    if contiune == 'no':
        wants_to_contiune = False
        print("Goodbye!\nThank you for BANKING WITH US!")