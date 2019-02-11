# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:44:06 2019

@author: Rozan
"""

#countofwords
#menghitung jumlah kata
W = ("saya","makan","nasi","goreng","di","rumah")
jumlahdata = {}
pw=len(W)
for i in range (pw):
    if W[i] in jumlahdata:
        jumlahdata[W[i]] += 1
    else:
        jumlahdata[W[i]] = 1
#menghitung jumlah kata 2    
from collections import Counter
counts = Counter(W)
print(counts)
#menghitung jumlah kata 3
def countWords(A):
    dic={}
    for i in A:
        if not i in dic:
            dic[i] = A.count(i)
    return dic

dic = countWords(W)
sorted_items=sorted(dic.items())

