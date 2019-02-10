from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import *


data = ["i","dont","like","green","and","ham","sam","i","am",'i','am','sam']
listOfBigrams = []
bigramCounts = {}
unigramCounts = {}
nbyn = {}
for i in range(len(data)):
	if i < len(data) - 1:

			listOfBigrams.append((data[i], data[i + 1]))

			if (data[i], data[i+1]) in bigramCounts:
				bigramCounts[(data[i], data[i + 1])] += 1
			else:
				bigramCounts[(data[i], data[i + 1])] = 1

	if data[i] in unigramCounts:
			unigramCounts[data[i]] += 1
	else:
		unigramCounts[data[i]] = 1



listOfProb = {}
for bigram in listOfBigrams:
		word1 = bigram[0]
		word2 = bigram[1]
		listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))

print(listOfProb)


