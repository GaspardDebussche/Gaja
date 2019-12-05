# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:42:46 2019

@author: 33766
"""

#Label of Gaja's states
#-2,-1,0,1,2
#not interesting,negative,interrogative,positive, all

#paw (0,1)
#eyes (0,1,2)
#sound (0,1,2,3)
#-2,-1,0,1,2

#for i in range(2):
#    for k in range(3):
#        for l in range(4):
#            print(str(i)+','+str(k)+','+str(l))

import pandas as pd
import numpy as np

dataset = pd.read_csv("./data/labelized_states.csv")

print(dataset)

transition_matrix = []
transition_matrix = np.zeros((len(dataset), len(dataset)))

for i in range(len(dataset)):
    
    if dataset['label'][i] == 0:
        s=0
        for j in range(len(dataset)):
            transition_matrix[i][j] = 1/len(dataset)
    
    if dataset['label'][i] == 1:
        s=0
        for j in range(len(dataset)):
            if dataset['label'][j] == -1:
                s+=1
                print(s)
        for j in range(len(dataset)):
            if dataset['label'][j] != -1:
                transition_matrix[i][j] = 1/(len(dataset)-s)
                
    if dataset['label'][i] == -1:
        s=0
        for j in range(len(dataset)):
            if dataset['label'][j] == 1:
                s+=1
        for j in range(len(dataset)):
            if dataset['label'][j] != 1:
                transition_matrix[i][j] = 1/(len(dataset)-s)
                
    if dataset['label'][i] == -2 or dataset['label'][i] == 2:
        s=0
        for j in range(len(dataset)):
            transition_matrix[i][j] = 1/len(dataset)
            
            
                
        
print(transition_matrix)

for i in range(len(dataset)):
    s=0
    for j in range(len(dataset)):
        s+=transition_matrix[i][j]
    print(s)