from tokenizer import tokenize, tokenizeMult, tokenizePos
from vigenereCipher import indexOfCoincidence, decrpytVigenere
import sys
'''
if len(sys.argv) != 2:
    print("Incorrect usage.")
    print('Usage: python hillTools.py cipherText.txt')
    sys.exit()

f = open(str(sys.argv[1]))
cipherText = f.read()
f.close()'''

cipherText = "ZCEKKIYWXOTQKRPBKSRRIZTPHWYJGBOVKZQOKGDFRWXEOBRPGMLSVSLUORPQZWNDRPZWNYTQJGZIIZTPHSCVVZLFKCYHLCZWOBQUUBERLHSHUHSHXPZWNPCHGHSHOBLQJCFWGHEKKGLPKFLWKPZWNGERVKSHTHTUKRMRZVRRLCCZGFOZNSYUKGEHJPFWCVLWGRTILSCHTQPWNSPJUQWLSPPUOGWLQSLQOBDWXIXHTHEKGHTVUIERLOOMAGEPKBEKKDFWYVTVLCZWJCHQGBTQYHLQZHZRYCZQUFERUZLWKVPLYZTNKZJWUATVYOMHGIELLIWSGGDDMSZIYIYOOUSWZVCRAUSWNSEUKSDZNOEKKWDOUCVLTUQRXKSDZVPZGBEVOGLOROCRABOKOAMXZVPGUSDQUHHDTHEKGHMHIOFVKWELYOWOGFZXTRSLSSGHXMDWKDTVGBPILCCWHCEKVVJVOQLORMLQJGALXWEXGZWBHSNDAGPKKWXDMWYHYVTVMCLOZCMHKLEHXBLOGBOGOGEDTH"

cipherText = cipherText.strip()

unigramFreq = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
               'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406,
               'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
               'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074}
sortedUnigramFreq = sorted(
    unigramFreq.items(), key=lambda x: x[1], reverse=True)

print("Kasiski Test results on 2, 3, 4, 5")

for x in range(2, 6):
    nFreq = tokenizePos(cipherText, x)
    ngramFreq = sorted(nFreq.items(), key=lambda x: x[1][0], reverse=True)
    print('=======================================================')
    print(ngramFreq)

print('=======================================================')

cipherLen = len(cipherText)

print("IoC on Ciphertext:")
print(indexOfCoincidence(cipherText))
print()

flag = True
while(flag):
    print("Please enter what key length to calc the IoC for? e.x. 3")
    print("q to quit")

    m = input()
    if m == "q" or m == "Q":
        break

    newCipherText = ""

    m = int(m)

    for x in range(0, cipherLen, m):
        newCipherText = newCipherText + cipherText[x]

    print(indexOfCoincidence(newCipherText))

print("Enter how you'd like the cipher divided e.x 2 for two rows with the first having 0 2 4 6....")
m = input()

n = int(m)

rows = []

for x in range(n):
    rows.append("")

for x in range(0, cipherLen):
    rows[x % n] = rows[x % n] + cipherText[x]

print("Top 10 Unigrams in Engligh Language:")
for x in range(10):
    print(sortedUnigramFreq[x])
print("========================================================")

for x in rows:
    print(x)
    unigrams = tokenize(x, 1)
    unigramsSorted = sorted(unigrams.items(), key=lambda x: x[1], reverse=True)
    print(unigramsSorted)
    print('=======================================================')

print(decrpytVigenere(cipherText, "GOLD"))
