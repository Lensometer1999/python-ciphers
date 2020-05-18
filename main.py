from pip._vendor.distlib.compat import raw_input


def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    plain_text.lower()
    for i in range(len(plain_text)):
        char = plain_text[i]
        encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        print(encrypted_text)
        return


print("This is a program to make ciphers, you two choices are BLANK and BLANK")
cipher_pick = int(input("Pick your cipher type in 1 for Caesar Cipher, type in 2 for BLANK: "))

while cipher_pick != 1 or 2:
    if cipher_pick == 1:
        plain_text = raw_input("\nYou have chosen " + str(cipher_pick) +
                               " which means Caesar Cipher, Type in your plain text: ")
        break
    elif cipher_pick == 2:
        plain_text = raw_input("\nYou have chosen " + str(cipher_pick) +
                               " which means BLANK, Type in your plain text: ")
        shift = int(input("How letters to shift: "))
        break
    else:
        print("Not 1 and or 2")
print(caesar_cipher_encrypt(plain_text, shift))
