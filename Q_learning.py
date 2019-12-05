# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:11:19 2019

@author: 33766
"""

#A chaque étape, génération d'un nombre aléatoire entre -1, 0 et 1
#Pour former le quadruplet (le triplet de l'état de gaja + la polarité de la phrase prononcée)

######################### GAJA's cat ############################
import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from time import time

dataset = pd.read_csv("./data/labelized_gaja_states.csv")

print(dataset)

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

# Stochastication
for i in range(len(transition_matrix)):
    s=0
    for j in range(len(transition_matrix)):
        if transition_matrix[i][j] != 0:
            s+=1
    if s>0:
        for p in range(len(transition_matrix)):
            transition_matrix[i][p] = transition_matrix[i][p] / s
    else:
        transition_matrix[i][1] = 1
for i in range(len(transition_matrix)):
    print(sum(transition_matrix[i][:]))
    
# Reward : 
# 10 : the most positive triplet -> [i,18]
# -2 : -1 -> 0 ; 0 -> 1
# -5 : 1 -> 0 ; -1 -> 0 

reward_matrix = []
reward_matrix = np.zeros((len(dataset)*3, len(dataset)*3))

for i in range(len(dataset)*3):
    for j in range(len(dataset)*3):
        if (0 <= i <= 23 and 0 <= j <= 23) or (24 <= i <= 48 and 24 <= j <= 48) or (49 <= i <= 72 and 49 <= j <= 72):
            if j%24 == 18:
                reward_matrix[i][j] = 10
            elif dataset['label'][i%24] == 1 and dataset['label'][j%24] == 1:
                reward_matrix[i][j] = -2
            elif dataset['label'][i%24] == 0 and dataset['label'][j%24] == 1:
                reward_matrix[i][j] = -2
            elif dataset['label'][i%24] == -1 and dataset['label'][j%24] == 0:
                reward_matrix[i][j] = -2
            else:
                reward_matrix[i][j] = -5
        else:
            reward_matrix[i][j] = -5


print(transition_matrix)
print(reward_matrix)
######################### Constants #############################

state_size, action_size = transition_matrix.shape

total_episodes = 1000  #50000
total_test_episodes = 100
max_steps = 99

learning_rate = 0.7
gamma = 0.618


epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

#################### Q learning algorithm ########################

qtable = np.zeros((state_size, action_size))

start_training = time()
count_1, count_2 = 0, 0
for episode in tqdm(range(total_episodes)):
    
    # polarity definition
    p = 1
    polarity = random.random()
    if 0 <= polarity < 0.50:
        p = 1
    elif 0.5 <= polarity < 0.75:
        p = 0
    else:
        p = -1
    # gaja's state definition
    gaja_state = random.randint(0, 23)
    # global state defintion
    if p == 1:
        state = gaja_state + 48
    elif p == 0:
        state = gaja_state + 24
    else:
        state = gaja_state

    for step in range(max_steps):

        exp_exp_tradeoff = random.uniform(0,1)

        if exp_exp_tradeoff > epsilon:
            #Prend la meilleur action en fonction de l'état décidé avant (global state definition)
            action = np.argmax(qtable[state,:])
            count_1 += 1
        
        else:
            # Choisit une action aléatoire parmi les possibles
            action = np.random.choice([i for i in range(state_size)], p=transition_matrix[state,:])
            count_2 += 1

        new_state = action
        
        reward = reward_matrix[state, action]

        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * 
                                    np.max(qtable[new_state, :]) - qtable[state, action])
                
        state = new_state

        if state == 0: 
            break
        
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
    tqdm._instances.clear()

print("Training time is ", time() - start_training)

print(count_1, count_2, qtable)

######################## Reward system ############################

#rewards = []
#
#for episode in range(total_test_episodes):
#    state = random.randint(0, state_size-1)
#    total_rewards = 0
#
#    for step in range(max_steps):
#
#        action = np.argmax(qtable[state,:])
#        
#        new_state = action
#        reward = reward_matrix[state, action]
#        
#        total_rewards += reward
#        
#        if new_state == 0:
#            rewards.append(total_rewards)
#            break
#        state = new_state
#
#print('Average score is ', sum(rewards)/total_test_episodes)
#print('Maximum score is ', max(rewards))
