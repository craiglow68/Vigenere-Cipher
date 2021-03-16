from tokenizer import tokenize, tokenizeMult, tokenizePos
from vigenereCipher import indexOfCoincidence
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

print("Kasiski Test results on 2, 3, 4, 5")

for x in range(2, 6):
    nFreq = tokenizePos(cipherText, x)
    ngramFreq = sorted(nFreq.items(), key=lambda x: x[1][0], reverse=True)
    print('=======================================================')
    print(ngramFreq)

print('=======================================================')

print(indexOfCoincidence(cipherText))
