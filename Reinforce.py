# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:11:19 2019

@author: GaspardDebussche
"""

######################### GAJA's cat ############################




import numpy as np
from time import time
from tqdm import tqdm
import random

from transition_matrix import transition_matrix


#transition_matrix = np.random.dirichlet([0.5]*23, 23)



nb_questions = 50
reward_matrix = np.zeros((23*nb_questions, 23))

reward_matrix[:, 0] = 10


for line in reward_matrix:
    line[1:] = np.random.choice([0, 1], size=(22,), p=[1./3, 2./3])
    line[1:] = line[1:]*(-3) - 2



print(reward_matrix)
######################### Constants #############################

state_size, _ = transition_matrix.shape

total_episodes = 50000
total_test_episodes = 100
max_steps = 99

learning_rate = 0.7
gamma = 0.618

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

#################### Q learning algorithm ########################

qtable = np.zeros((state_size*nb_questions, state_size))

start_training = time()
count_1, count_2 = 0, 0
for episode in tqdm(range(total_episodes)):

    state = random.randint(0, state_size - 1)
    question = random.randint(0, nb_questions - 1)

    exp_exp_tradeoff = random.uniform(0, 1)

    if exp_exp_tradeoff > epsilon:
        action = np.argmax(qtable[state*nb_questions + question, :])
        count_1 += 1

    else:
        action = np.random.choice([i for i in range(state_size)], p=transition_matrix[state, :])
        count_2 += 1

    for step in range(max_steps):

        new_state = action
        new_question = random.randint(0, nb_questions - 1)

        exp_exp_tradeoff = random.uniform(0, 1)

        if exp_exp_tradeoff > epsilon:
            new_action = np.argmax(qtable[new_state*nb_questions + new_question, :])
            count_1 += 1

        else:
            new_action = np.random.choice([i for i in range(state_size)], p=transition_matrix[new_state, :])
            count_2 += 1

        reward = reward_matrix[state*nb_questions + question, action]

        qtable[state*nb_questions + question, action] = qtable[state*nb_questions + question, action] + \
                                            learning_rate * (
                                                    reward +
                                                    gamma *qtable[new_state*nb_questions + new_question, new_action] -
                                                    qtable[state*nb_questions + question, action]
                                                        )

        state = new_state
        action = new_action
        question = new_question


        if state == 0:
            break

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
    tqdm._instances.clear()

print("Training time is ", time() - start_training)

#    for step in range(max_steps):
print(count_1, count_2, qtable)

######################## Reward system ############################

#rewards = []

#for episode in range(total_test_episodes):
#    state = random.randint(0, state_size - 1)
#    total_rewards = 0
#
#
#        action = np.argmax(qtable[state, :])
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
#print('Average score is ', sum(rewards) / total_test_episodes)
#print('Maximum score is ', max(rewards))
