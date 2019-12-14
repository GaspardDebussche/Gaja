# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:57:00 2019

@author: 33766
"""

""" IMPORTS """
import pandas as pd
import numpy as np
from textblob import TextBlob
import random
import nltk

dataset = pd.read_csv("./data/labelized_states.csv")

lexicon = {"green" : [3,4,5,6,15,16,17,18], "red": [], "paw": [], "sound": [], "tell": [], "discuss": [], "say": []}

positive_behaviour = [0, 3, 4, 12, 15, 16]
neutral_behaviour = [2, 6, 10, 14, 18, 22]
negative_behaviour = [1, 7, 9, 13, 19, 21]
no_sense_behaviour = [5, 8, 17, 20]

#sentence = "show me your pretty blue eyes beautiful cat!"
#input_string = "you are a little bastard, die shit !"

def reward(input_string, rate = 0.2):
    reward_matrix = np.zeros((23, 23))
    case = 0
    sentence = TextBlob(input_string)
    selection = [i for i in range(0,23)]
    
    # 10-reward choice
    if sentence.sentiment.polarity >= rate:
        selection = positive_behaviour
        case = 1
    if sentence.sentiment.polarity <= -rate:
        selection = negative_behaviour
        case = -1
    if -rate < sentence.sentiment.polarity < rate:
        selection = neutral_behaviour
        case = 0
    for w in nltk.word_tokenize(input_string):
        if w in lexicon.keys():
            if sentence.sentiment.polarity >= 0.2:
                selection = list(set(selection) & set(lexicon[w]))
    
    #Matrix generation
    for i in range(len(reward_matrix)):
        if case == 1:
            for j in range(len(reward_matrix)):
                if 1 in [dataset['paw'][j], dataset['eyes'][j], dataset['voice'][j]]:
                    reward_matrix[i][j]= -2
                else:
                    reward_matrix[i][j]= -5
        if case == -1:
            for j in range(len(reward_matrix)):
                if 2 in [dataset['paw'][j], dataset['eyes'][j], dataset['voice'][j]]:
                    reward_matrix[i][j]= -2
                else:
                    reward_matrix[i][j]= -5
        if case == 0:
            for j in range(len(reward_matrix)):
                if 0 in [dataset['paw'][j], dataset['eyes'][j], dataset['voice'][j]]:
                    reward_matrix[i][j]= -2
                else:
                    reward_matrix[i][j]= -5
                
    r = random.choice(selection)
    reward_matrix[:,r] = 10
    return(reward_matrix)


#print(reward(input_string)) 