
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ecrypt(text, shift):
    new_letter = []
    for letter in text:
        new_index = alphabet.index(letter) + shift

        while(new_index > 25):
            new_index -= 26

        new_letter.append(alphabet[new_index])

    print(f"The encoded text is {''.join(new_letter)}")

ecrypt(text, shift)

def decrypt(text, shift):
    new_letter = []
    for letter in text:
        new_index = alphabet.index(letter) - shift

        while(new_index < 0):
            new_index += 26

        new_letter.append(alphabet[new_index])

    print(f"The decoded text is {''.join(new_letter)}")

decrypt("jgnnqyqtnf", shift)


