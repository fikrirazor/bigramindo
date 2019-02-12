
# coding: utf-8

# In[1]:


# BIGRAM PROGRAM


# In[2]:


#Import libraries
from collections import OrderedDict
import heapq 
import pandas as pd
from nltk import word_tokenize


# In[3]:


wt = word_tokenize
#memasukan data csv menggunakan pandas
data = pd.read_csv('data artikel kompas/artikel.csv', encoding='latin-1')
data.head()


# In[4]:


data.tail()


# In[5]:


#tokenisasi menggunakan nltk
datatoken = data.apply(lambda row: wt(row['Berita']), axis=1)
print(datatoken.head(10))


# In[6]:


#dari pandas ke list
datatoken = datatoken.values.tolist()
print(datatoken)


# In[7]:


#join list of list
datatoken = sum(datatoken, [])
print(datatoken)


# In[8]:


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


# In[9]:


valueprob = OrderedDict()
listOfProb = {}
for bigram in listOfBigrams:
    word1 = bigram[0]
    word2 = bigram[1]
    listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))  
    valueprob[word1+" "+word2] = listOfProb.get(bigram)
       
uniprob = {}
for unigram in datatoken:
    uniprob[unigram] = 1/ unigramCounts.get(unigram)


# In[10]:


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


# In[12]:


testset = 'sam','am','hate'
"""  PERPLEXITY """  
perplexity = 1
N = 0

for i in testset:
    if i in uniprob:
        N += 1
        perplexity = perplexity * (1/uniprob[i])
        
perplexity = pow(perplexity, 1/float(N))
print(perplexity)


# In[13]:


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

