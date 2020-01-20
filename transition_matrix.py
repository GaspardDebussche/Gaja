# -*- coding: utf-8 -*-

""" IMPORTS """
import pandas as pd
import numpy as np

#Dataset loading
dataset = pd.read_csv("./data/labelized_states.csv")

""" TRANSITION MATRIX DEFINITION """

def transition_m():
    transition_matrix = np.zeros((len(dataset), len(dataset)))
    
    for i in range(len(dataset)):
        for j in range(len(dataset)):
            if (abs(dataset['paw'][i]-dataset['paw'][j]) <= 2 and 
                abs(dataset['eyes'][i] - dataset['eyes'][j]) == 0 and
                abs(dataset['voice'][i]- dataset['voice'][j]) == 0):
                transition_matrix[i][j] = 1
            elif (abs(dataset['paw'][i]-dataset['paw'][j]) == 0 and 
                abs(dataset['eyes'][i] - dataset['eyes'][j]) <= 2 and
                abs(dataset['voice'][i]- dataset['voice'][j]) == 0):
                transition_matrix[i][j] = 1
            elif (abs(dataset['paw'][i]-dataset['paw'][j]) == 0 and 
                abs(dataset['eyes'][i] - dataset['eyes'][j]) == 0 and
                abs(dataset['voice'][i]- dataset['voice'][j]) <= 1):
                transition_matrix[i][j] = 1
            else:
                transition_matrix[i][j] = 0
                
    for i in range(len(dataset)):
        s=0
        for j in range(len(dataset)):
            if transition_matrix[i][j] > 0:
                s+=transition_matrix[i][j]
        for j in range(len(dataset)):
            transition_matrix[i][j] = transition_matrix[i][j]/s
            
    return(transition_matrix)

