import re
import string


def vigenere_cipher(message, keyword):
    message = re.sub('\W+', '', message).lower()
    encrypted_message = []
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
        cipher.append((msg_ascii, key_ascii))
        i += 1
        j += 1
    print(cipher)
    for msg, key in cipher:
        if msg + key > 25:
            encrypted_message.append(alphabet[(msg+key)-26])
        else:
            encrypted_message.append(alphabet[msg + key])

    return "".join(encrypted_message).upper()


message = "Why is a raven like a writing desk"
keyword = "rabbithole"
print(vigenere_cipher(message, keyword))
