# Author: Jacob Craiglow
# Description: Contains tools for tokenizing a string into nGrams of your chosen size

# Builds and counts nGrams from text.
# Returns a dictionary of nGrams and their counts.
# text - text to analyze.
# ngram - the size of the nGrams.
# 1 for one character strings. 2 for two character strings, etc.
# Do not put 0 and do not exceed the length of the cipher text.


def tokenize(text, ngram):
    textLength = len(text)
    ngramFreq = {}

    for index in range(textLength - (ngram - 1)):
        textSnippet = text[index:index+ngram]

        if textSnippet in ngramFreq:
            ngramFreq[textSnippet] = ngramFreq[textSnippet] + 1
        else:
            ngramFreq[textSnippet] = 1

    return ngramFreq


def tokenizeMult(text, ngram):
    textLength = len(text)
    tempDict = {}
    ngramFreq = {}

    for index in range(textLength - (ngram - 1)):
        textSnippet = text[index:index+ngram]

        if textSnippet in ngramFreq:
            ngramFreq[textSnippet] = ngramFreq[textSnippet] + 1
        else:
            if textSnippet in tempDict:
                ngramFreq[textSnippet] = 2
            else:
                tempDict[textSnippet] = 1

    return ngramFreq


def tokenizePos(text, ngram):
    textLength = len(text)
    tempDict = {}
    ngramFreq = {}

    for index in range(textLength - (ngram - 1)):
        textSnippet = text[index:index+ngram]

        if textSnippet in ngramFreq:
            ngramFreq[textSnippet][0] = ngramFreq[textSnippet][0] + 1
            ngramFreq[textSnippet][1].append(index)
        elif textSnippet in tempDict:
            ngramFreq[textSnippet] = tempDict[textSnippet]
            ngramFreq[textSnippet][0] = 2
            ngramFreq[textSnippet][1].append(index)
        else:
            tempDict[textSnippet] = [1, [index]]

    return ngramFreq
