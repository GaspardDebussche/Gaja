# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:07:04 2019

@author: 33766
"""

""" IMPORTS """
import pandas as pd
import numpy as np
from textblob import TextBlob
import random
import nltk

dataset = pd.read_csv("./data/labelized_states.csv")

lexicon = {"green" : [3, 4, 5, 6, 15, 16, 17, 18], 
           "eyes" : [3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22],
           "red": [7, 8, 9, 10, 19, 20, 21, 22], 
           "paw": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 
           "sound": [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22], 
           "tell": [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22],
           "discuss": [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22],
           "say": [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22]}

#paw =[]
#eyes=[]
#green=[]
#red=[]
#voice=[]
#for i in range(len(dataset)):
#    if dataset['paw'][i]==1:
#        paw.append(i)
#    if dataset['eyes'][i]==1 or dataset['eyes'][i]==2:
#        eyes.append(i)
#    if dataset['eyes'][i]==1:
#        green.append(i)
#    if dataset['eyes'][i]==2:
#        red.append(i)
#    if dataset['voice'][i]==1 or dataset['voice'][i]==2 or dataset['voice'][i]==3:
#        voice.append(i)
#        
#print(voice)


positive_behaviour = [0, 3, 4, 11, 12, 15, 16]
interrogative_behaviour = [2, 6, 10, 14, 18, 22]
negative_behaviour = [1, 7, 9, 13, 19, 21]
no_sense_behaviour = [5, 8, 17, 20]

#for i in range(len(dataset)):
#    if dataset['label'][i] == -2:
#        no_sense_behaviour.append(i)
#    if dataset['label'][i] == -1:
#        negative_behaviour.append(i)
#    if dataset['label'][i] == 0:
#        interrogative_behaviour.append(i)
#    if dataset['label'][i] == 1:
#        positive_behaviour.append(i)
#        
#print(positive_behaviour, interrogative_behaviour, negative_behaviour, no_sense_behaviour)

#sentence = "show me your pretty blue eyes beautiful cat!"
#input_string = "you are a little bastard, die shit !"

def reward_m(input_string, rate = 0.2):
    reward_matrix = np.zeros((23, 23))
    case = 0
    sentence = TextBlob(input_string)
    selection = [i for i in range(0,23)]
    
    # 10-reward choice
    print(sentence.sentiment.polarity)
    if sentence.sentiment.polarity >= rate:
        selection = positive_behaviour
        case = 1
    if sentence.sentiment.polarity <= -rate:
        selection = negative_behaviour
        case = -1
    if -rate < sentence.sentiment.polarity < rate:
        selection = interrogative_behaviour
        case = 0
    for w in nltk.word_tokenize(input_string):
        if w in lexicon.keys():
            if sentence.sentiment.polarity >= 0.2:
                selection = list(set(selection) & set(lexicon[w]))

# label
# -2 no sense -1 negative 0 interrogative 1 positive
    #Matrix generation
    for i in range(len(reward_matrix)):
        if case == 1:
            for j in range(len(reward_matrix)):
                if dataset['label'][j] == 1:
                    reward_matrix[i][j]= -2
                else:
                    reward_matrix[i][j]= -5
        if case == -1:
            for j in range(len(reward_matrix)):
                if dataset['label'][j] == -1:
                    reward_matrix[i][j]= -2
                else:
                    reward_matrix[i][j]= -5
        if case == 0:
            for j in range(len(reward_matrix)):
                if dataset['label'][j] == 0:
                    reward_matrix[i][j]= -2
                else:
                    reward_matrix[i][j]= -5
                
    r = random.choice(selection)
    reward_matrix[:,r] = 10
    return(reward_matrix)


#print(reward(input_string)) 