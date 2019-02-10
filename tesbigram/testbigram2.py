# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:44:06 2019

@author: Rozan
"""

S = [1,2,3,4,5,6]
A = [1,2,3,4,5]
B = [2,4,6]

s=len(S)
a=len(A)
b=len(B)
iab=len(list(set(A) & set(B))) 
peluanga = a/s 
peluangb = b/s
peluangiab = iab/s
peluangAdengansyaratB = peluangiab/peluangb
tespeluang = (peluanga*peluangb)/peluangb

W = ("saya","makan","nasi","goreng","di","rumah")

w = len(W)
wkurang1 = len(W)-1
peluangw=w/w
peluangwkurang1 = wkurang1/w
peluangwndengansyaratwnkurang1 = (peluangw*peluangwkurang1)/peluangwkurang1

