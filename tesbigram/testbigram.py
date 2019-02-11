from collections import OrderedDict
import heapq 

"""  MODEL BIGRAM """ 
data = ["i","dont","like","green","and","ham","sam","i","am",'i','am','sam']
testset = 'sam','am','hate'
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


  
"""  HITUNG PELUANG BIGRAM DAN UNIGRAM """ 
valueprob = OrderedDict()
listOfProb = {}
for bigram in listOfBigrams:
    word1 = bigram[0]
    word2 = bigram[1]
    listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))  
    valueprob[word1+" "+word2] = listOfProb.get(bigram)
       
uniprob = {}
for unigram in data:
    uniprob[unigram] = 1/ unigramCounts.get(unigram)
    
"""  ADD ONE SMOTHING """ 
def addOneSmothing(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    cStar = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        listOfProb[bigram] = (bigramCounts.get(bigram) + 1)/(unigramCounts.get(word1) + len(unigramCounts))
        cStar[bigram] = (bigramCounts[bigram] + 1) * unigramCounts[word1] / (unigramCounts[word1] + len(unigramCounts))
        return listOfProb, cStar
      
#addOneSmothing(listOfBigrams, unigramCounts, bigramCounts)
    
"""  PERPLEXITY """  
perplexity = 1
N = 0

for i in testset:
    if i in uniprob:
        N += 1
        perplexity = perplexity * (1/uniprob[i])
        
perplexity = pow(perplexity, 1/float(N))
print(perplexity)



"""  PREDIKSI KATA YANG 	AKAN MUNCUL"""

matchedBigrams = []
checkForThisBigram = 'i'
topDict = {}  
for bigram in listOfBigrams:
    if checkForThisBigram == bigram[0]:
            matchedBigrams.append(bigram[0]+" "+bigram[1])
         
            
print(matchedBigrams)            
	
for singleBigram in matchedBigrams:
		topDict[singleBigram] = valueprob[singleBigram]

topBigrams = heapq.nlargest(5, topDict, key=topDict.get)
for b in topBigrams:
		print( b+" : "+str(topDict[b])+"\n")

#print(unigramCounts)    
#print(uniprob)
#print(listOfBigrams)