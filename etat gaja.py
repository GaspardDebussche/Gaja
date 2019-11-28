# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:30:36 2019

@author: 33766
"""

#Gaja's states
#0,1,2,3,4,5,6
#N,p,eb,er,sp,si,sn
#Neurtral, give the paw, blue eyes, red eyes, positive sound, interrogative sound, negative sound

#Label of Gaja's states
#None,-2,-1,0,1
#Impossible,not interesting,negative,interrogative,positive

import pandas as pd
import numpy as np

dataset = pd.read_csv("./data/labelized_gaja_states.csv")

print(dataset)

# transition matrix + reward

# TRANSITION MATRIX RULES

transition_matrix_positive = []

transition_matrix_positive = np.zeros((len(dataset), len(dataset)))

for i in range(len(dataset)):
    for j in range(len(dataset)):
        if dataset['label'][i] == 1 and dataset['label'][j] == 1:
            transition_matrix_positive[i][j] = 1
        elif dataset['label'][i] == -1 and dataset['label'][j] == 0:
            transition_matrix_positive[i][j] = 1
        elif dataset['label'][i] == 0 and dataset['label'][j] == 1:
            transition_matrix_positive[i][j] = 1
        else:
            transition_matrix_positive[i][j] = 0
            
#print(transition_matrix_positive)

transition_matrix_negative = []

transition_matrix_negative = np.zeros((len(dataset), len(dataset)))

for i in range(len(dataset)):
    for j in range(len(dataset)):
        if dataset['label'][i] == 1 and dataset['label'][j] == 0:
            transition_matrix_negative[i][j] = 1
        elif dataset['label'][i] == -1 and dataset['label'][j] == -1:
            transition_matrix_negative[i][j] = 1
        elif dataset['label'][i] == 0 and dataset['label'][j] == -1:
            transition_matrix_negative[i][j] = 1
        else:
            transition_matrix_negative[i][j] = 0
            
#print(transition_matrix_negative)


transition_matrix_neutral = []

transition_matrix_neutral = np.zeros((len(dataset), len(dataset)))

for i in range(len(dataset)):
    for j in range(len(dataset)):
        if dataset['label'][i] == 1 and dataset['label'][j] == 0:
            transition_matrix_neutral[i][j] = 1
        elif dataset['label'][i] == -1 and dataset['label'][j] == 0:
            transition_matrix_neutral[i][j] = 1
        elif dataset['label'][i] == 0 and dataset['label'][j] == 0:
            transition_matrix_neutral[i][j] = 1
        else:
            transition_matrix_neutral[i][j] = 0
            
#print(transition_matrix_neutral)

# Big transition matrix

#0 - 23 : -1
#7 - 13 : 0
#14 - 20 : 1

print(len(dataset))
transition_matrix = []

transition_matrix = np.zeros((len(dataset)*3, len(dataset)*3))

for j in range(len(dataset)*3):
    if 0<= j <= 23:
        # Negative sentence
        for i in range(len(dataset)*3):
            if 0 <= i <= 23:
                if dataset['label'][i] == 1 and dataset['label'][j] == 0:
                    transition_matrix[i][j] = 1
                elif dataset['label'][i] == -1 and dataset['label'][j] == -1:
                    transition_matrix[i][j] = 1
                elif dataset['label'][i] == 0 and dataset['label'][j] == -1:
                    transition_matrix[i][j] = 1
                else:
                    transition_matrix[i][j] = 0
            else:
                transition_matrix[i][j] = 0
    elif 24 <= j <= 48:
        for i in range(len(dataset)*3):
            if 24 <= i <= 48:
                if dataset['label'][i%24] == 1 and dataset['label'][j%24] == 0:
                    transition_matrix[i][j] = 1
                elif dataset['label'][i%24] == -1 and dataset['label'][j%24] == 0:
                    transition_matrix[i][j] = 1
                elif dataset['label'][i%24] == 0 and dataset['label'][j%24] == 0:
                    transition_matrix[i][j] = 1
                else:
                    transition_matrix[i][j] = 0
            else:
                transition_matrix[i][j] = 0
    else:
        for i in range(len(dataset)*3):
            if 49 <= i <= 72:
                if dataset['label'][i%24] == 1 and dataset['label'][j%24] == 1:
                    transition_matrix[i][j] = 1
                elif dataset['label'][i%24] == -1 and dataset['label'][j%24] == 0:
                    transition_matrix[i][j] = 1
                elif dataset['label'][i%24] == 0 and dataset['label'][j%24] == 1:
                    transition_matrix[i][j] = 1
                else:
                    transition_matrix[i][j] = 0
            else:
                transition_matrix[i][j] = 0
        
print(transition_matrix)

# Reward : 
# 10 : the most positive triplet -> [i,18]
# -2 : -1 -> 0 ; 0 -> 1
# -5 : 1 -> 0 ; -1 -> 0 

reward_matrix = []
reward_matrix = np.zeros((len(dataset), len(dataset)))

for i in range(len(dataset)):
    for j in range(len(dataset)):
        if j == 18:
            reward_matrix[i][j] = 10
        elif dataset['label'][i] == 1 and dataset['label'][j] == 1:
            reward_matrix[i][j] = -2
        elif dataset['label'][i] == 0 and dataset['label'][j] == 1:
            reward_matrix[i][j] = -2
        elif dataset['label'][i] == -1 and dataset['label'][j] == 0:
            reward_matrix[i][j] = -2
        else:
            reward_matrix[i][j] = -5
            
print(reward_matrix)