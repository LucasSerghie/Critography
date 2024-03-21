"""Implementation of Belaso cipher"""
import string


def encipher(code, key):
    "First we turn the code and key to uppercase letters"
    key = key.upper()
    code = code.upper()

    "Second step is to compute the vector of steps for each letter in the key"
    alphabet = string.ascii_uppercase
    shift = list()
    for i in key:
        for j in range(0, len(alphabet)):
            if alphabet[j] == i:
                shift.append(j)

    "Next using the vector with steps we can now encipher the code"
    k = 0
    encoded = ""
    for i in range(0, len(code)):
        if 64 < ord(code[i]) < 91:
            if ord(code[i]) + shift[k] > 90:
                encoded += chr(ord('A') + (ord(code[i]) + shift[k] - ord('Z')))
            else:
                encoded += chr(ord(code[i]) + shift[k])
            k += 1
            if k == len(shift) - 1:
                k = 0
        elif code[i] == ' ':
            encoded += ' '

    print("encrypted version: ", encoded)


_key = "bbcd"
_code = "Today is monday"
print("Original version: ", _code, "\n")


encipher(_code, _key)
