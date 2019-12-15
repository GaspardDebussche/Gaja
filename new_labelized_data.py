# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:54:10 2019

@author: 33766
"""
#New to have a coherence in the distances
#-1, 0, 1, 2
# negative / neutre / interrogative / positive
  
# past codes
#0, 1, 2, 3
#neutre / positif / negative / interrogative


import pandas as pd
dataset = pd.read_csv("./data/labelized_states.csv")

#paw,eyes,voice,label

for i in range(len(dataset)):
    if dataset['paw'][i]==1:
        dataset['paw'][i] = 2
    if dataset['eyes'][i]== 2:
        dataset['eyes'][i] = -1
    if dataset['eyes'][i]== 1:
        dataset['eyes'][i] = 2
    if dataset['voice'][i]== 2:
        dataset['voice'][i] = -1
    if dataset['voice'][i]== 1:
        dataset['voice'][i] = 2
    if dataset['voice'][i]==3 :
        dataset['voice'][i] = 1

print(dataset)

#dataset.to_csv("./data/new_labelized_states.csv")