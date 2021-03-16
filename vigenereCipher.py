from tokenizer import tokenize


def decrpytVigenere(cipherText, key):
    plainText = ""
    keyLen = len(key)
    count = 0

    for char in cipherText:
        decryptedChar = chr(
            (((ord(char)-65) - (ord(key[count])-65)) % 26) + 65)
        plainText = plainText + decryptedChar

        count += 1

        if count == keyLen:
            count = 0

    return plainText


def encrpytVigenere(plainText, key):
    cipherText = ""
    keyLen = len(key)
    count = 0

    for char in plainText:
        encryptedChar = chr(
            (((ord(char)-65) + (ord(key[count])-65)) % 26) + 65)
        cipherText = cipherText + encryptedChar

        count += 1

        if count == keyLen:
            count = 0

    return cipherText


def indexOfCoincidence(cipherText):
    indexOfCoincidence = 0
    cipherLen = len(cipherText)
    unigramFreqs = tokenize(cipherText, 1)

    for x in unigramFreqs.keys():
        temp = (unigramFreqs[x]/float(cipherLen))
        temp2 = ((unigramFreqs[x] - 1)/float(cipherLen - 1))
        indexOfCoincidence = indexOfCoincidence + (temp * temp2)

    return indexOfCoincidence
