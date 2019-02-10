# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:05:38 2019

@author: Rozan
"""

import pandas as pd
from nltk import word_tokenize

wt = word_tokenize
#memasukan data csv menggunakan pandas
data = pd.read_csv('data artikel kompas/artikel.csv', encoding='latin-1')
#tokenisasi menggunakan nltk
datatoken = data.apply(lambda row: wt(row['Berita']), axis=1)
#dari pandas ke list
datatoken = datatoken.values.tolist()
#join list of list
datatoken = sum(datatoken, [])


listOfBigrams = []
bigramCounts = {}
unigramCounts = {}
nbyn = {}
for i in range(len(datatoken)):
	if i < len(datatoken) - 1:

			listOfBigrams.append((datatoken[i], datatoken[i + 1]))

			if (datatoken[i], datatoken[i+1]) in bigramCounts:
				bigramCounts[(datatoken[i], datatoken[i + 1])] += 1
			else:
				bigramCounts[(datatoken[i], datatoken[i + 1])] = 1

	if datatoken[i] in unigramCounts:
			unigramCounts[datatoken[i]] += 1
	else:
		unigramCounts[datatoken[i]] = 1



listOfProb = {}
for bigram in listOfBigrams:
		word1 = bigram[0]
		word2 = bigram[1]
		listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))

print(listOfProb)
        
