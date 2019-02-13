
# coding: utf-8

# In[1]:


# BIGRAM PROGRAM


# In[2]:


#Import libraries
from collections import OrderedDict
import heapq 
import pandas as pd
from nltk import word_tokenize
import string


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
#print(datatoken.head(10))


# In[6]:


#dari pandas ke list
datatoken = datatoken.values.tolist()
#print(datatoken)


# In[7]:
"""  PREPROCESSING """ 

#join list of list
datatoken = sum(datatoken, [])
datatoken = [w.lower() for w in datatoken]
datatoken= [''.join(c for c in s if c not in string.punctuation) for s in datatoken]
datatoken = [s for s in datatoken if s]
#print(datatoken)


# In[8]:
"""  MEMBUAT MODEL BIGRAM """ 

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
"""  PELUANG BIGRAM & UNIGRAM """ 

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
#print(bigramCounts)   
#print(unigramCounts)    
#print(uniprob)
#print(listOfProb)

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
      
addOneSmothing(listOfBigrams, unigramCounts, bigramCounts)


# In[12]:
"""  MENGHITUNG PELUANG BIGRAM """ 
print('=================== MENGHITUNG PELUANG KATA ==================')
teskata = []

valuekata = OrderedDict()
tesvalue = OrderedDict()
test1 = ['hujan','lebat','sehingga','akan']
test2 = ['saya','makan','nasi']
test3 = ['hari','ini','libur']
test4 = ['berita','ini','sangat','membantu'] 
test5 = ['pada','tanggal','23']
a = 0
print("\n Kalimat :"+str(test5))
for i in range(len(test5)):
	 if i < len(test5) - 1:
			teskata.append((test5[i], test5[i + 1]))
print("\n Bigram :"+str(teskata))
for word in teskata:
    word1 = word[0]
    word2 = word[1]
    tesvalue[word1+" "+word2] = 0

    
for key in tesvalue:
     if key in valueprob:       
        valuekata[key] = valueprob[key]
 
hasil = 1
for key in tesvalue:
     if key in valuekata:       
        tesvalue[key] = valuekata.get(key)
        
for value in tesvalue:
        a = tesvalue.get(key) 
        hasil *= a    
    
                
print("\n Nilai Peluang Bigram :"+str(tesvalue))
print("\n Hasil Peluang :"+str(hasil))


# In[13]:


"""  PREDIKSI KATA YANG 	AKAN MUNCUL"""
print('\n =================== PREDIKSI  KATA SELANJUTNYA ==================')
matchedBigrams = []
checkForThisBigram = 'kendaraan'
print("Kalimat :\n"+str(checkForThisBigram))
lastword = checkForThisBigram
topDict = {}  
for bigram in listOfBigrams:
    if lastword == bigram[0]:
            matchedBigrams.append(bigram[0]+" "+bigram[1])
         
            
#print(matchedBigrams)            
	
for singleBigram in matchedBigrams:
		topDict[singleBigram] = valueprob[singleBigram]

topBigrams = heapq.nlargest(10, topDict, key=topDict.get)

for b in topBigrams:
		print( b+" : "+str(topDict[b])+"\n")
        

# In[14]:
print('\n =================== PERPLEXITY MODEL  ==================')       
testset = []
testset = 'penampakan','bulan'
"""  PERPLEXITY """
perplexity = 1
N = 0

for i in testset:
    if i in uniprob:
        N += 1
        perplexity = perplexity * (1/uniprob[i])

perplexity = pow(perplexity, 1/float(N))
print("testset :"+str(testset))
print("perplexity :"+str(perplexity))
