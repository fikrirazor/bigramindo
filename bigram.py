# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:05:38 2019

@author: Rozan
"""

import pandas as pd
from nltk import word_tokenize
wt = word_tokenize
data = pd.read_csv('data artikel kompas/artikel.csv', encoding='latin-1')

datatoken = data.apply(lambda row: wt(row['Berita']), axis=1)

        
