def caesarCipherEncryptor(string, key):
    key = key % 26
    newString = ''
    for char in string:
        newString += getNewValue(char, key)
    return newString


def getNewValue(char, key):
    newAscii = ord(char) + key
    if newAscii < 97:
        newAscii = 123 - (97 - newAscii)
    if newAscii > 122:
        newAscii = 96 + (newAscii - 122)
    return chr(newAscii)
