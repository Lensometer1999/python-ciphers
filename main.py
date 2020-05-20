from pip._vendor.distlib.compat import raw_input

def substitution_cipher_encrypt(plain_text, associations):
    out = ""
    plain_text = plain_text.lower()
    for letter in plain_text:
        if letter in associations:
            out += associations[letter]
    return out

# funciton for caesar cipher
def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    plain_text.lower()
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char != chr(32):
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += chr(32)
    return encrypted_text


def caesar_cipher_decrypt(cipher_text, shift):
    decrypted_text = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char != chr(32):
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += chr(32)
    return decrypted_text


print("This is a program to make ciphers, you two choices are BLANK and BLANK")
cipher_pick = int(input("Pick your cipher type in 1 for Caesar Cipher, type in 2 for BLANK: "))

num = 0
text = ""

while cipher_pick != 1 or 2:
    if cipher_pick == 1:
        text = raw_input("\nYou have chosen " + str(cipher_pick) +
                         " which means Caesar Cipher, Type in your plain text: ")
        num = int(input("How many letters do you want to shift: "))
        break
    elif cipher_pick == 2:
        text = raw_input("\nYou have chosen " + str(cipher_pick) +
                         " which means BLANK, Type in your plain text: ")

        break
    else:
        print("Not 1 and or 2")
print(caesar_cipher_encrypt(text, num))
print(caesar_cipher_decrypt(caesar_cipher_encrypt(text, num), num))