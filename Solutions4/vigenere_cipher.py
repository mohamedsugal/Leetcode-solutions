import re
import string


def vigenere_cipher(message, keyword):
    message = re.sub('\W+', ' ', message).lower().rstrip()
    encrypted_message = ""
    alphabet = {}
    for i, char in enumerate(string.ascii_lowercase):
        alphabet[i] = char

    cipher = []
    i, j = 0, 0
    while i < len(message):
        if j == len(keyword):
            j = 0
        msg_ascii = ord(message[i]) - ord('a')
        key_ascii = ord(keyword[j]) - ord('a')
        if message[i] == " ":
            cipher.append((msg_ascii, 0))
            i += 1
        else:
            cipher.append((msg_ascii, key_ascii))
            i += 1
            j += 1

    for msg, key in cipher:
        if msg + key > 25:
            encrypted_message += alphabet[(msg+key)-26]
        elif msg < 0:
            encrypted_message += chr(32)
        else:
            encrypted_message += alphabet[msg + key]

    return encrypted_message


message = "Make It happen?"
keyword = "math"
print(vigenere_cipher(message, keyword))
