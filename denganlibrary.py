# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:12:38 2019

@author: Rozan
"""




import matplotlib
import numpy as np
import pandas as pd

from scipy.sparse import csr_matrix, hstack
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import CountVectorizer
matplotlib.style.use('ggplot')
from nltk import word_tokenize
import pandas as pd

wt = word_tokenize
#memasukan data csv menggunakan pandas
data = pd.read_csv('data artikel kompas/artikel.csv', encoding='latin-1')
vectorizer = CountVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1)
name_corpus = data.Berita.tolist()
X = vectorizer.fit_transform(name_corpus).toarray()
print('ngram.shape: {0}'.format(X.shape))
