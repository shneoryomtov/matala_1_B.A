# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:01:56 2023

@author: shneo
"""


#Q_2
def revword(word):
    word = word[::-1].lower()
    return word



def countword ():
    caunt = dict()      
    fmane = "C:/Users/shneo/OneDrive/exc_phyton/text.txt"
    file = open(fmane)
    for x in file:
        t = x.split()
        first_word = t[0]
        caunt[first_word] = 1
        break


    for line in file:
        line = revword(line)
        line = line.split()
        for word in line:
            if word in caunt:
                caunt[word] = caunt.get(word,0) +1
    return caunt[first_word]
            
print(countword())