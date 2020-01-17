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

from transition_matrix import transition_m
from reward_matrix import reward_m

######################### Constants #############################


def reinforcement_learning(sentence, input_state):
    transition_matrix = transition_m()
    reward_matrix = reward_m(sentence)
    
    state_size, _ = transition_matrix.shape

    total_episodes = 1000
    total_test_episodes = 100
    max_steps = 99

    learning_rate = 0.7
    gamma = 0.618

    epsilon = 1.0
    max_epsilon = 1.0
    min_epsilon = 0.01
    decay_rate = 0.01

    #################### Q learning algorithm ########################

    state_size, action_size = transition_matrix.shape

    qtable = np.zeros((state_size, action_size))

    start_training = time()
    count_1, count_2 = 0, 0
    for episode in tqdm(range(total_episodes)):
        state = random.randint(0, state_size-1)

        for step in range(max_steps):

            exp_exp_tradeoff = random.uniform(0,1)

            if exp_exp_tradeoff > epsilon:
                action = np.argmax(qtable[state,:])
                count_1 += 1

            else:
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

    #print(qtable)

    #print("Training time is ", time() - start_training)

    #    for step in range(max_steps):
    #print(reward_matrix)

    ######################## Reward system ############################

    rewards = []
    state = input_state
    total_rewards = 0
    states = [state]

    for step in range(max_steps):

        action = np.argmax(qtable[state,:])

        new_state = action
        states.append(new_state)
        reward_value = reward_matrix[state, action]


        total_rewards += reward_value

        if reward_value == 10:
            rewards.append(total_rewards)
            break
        state = new_state


    #print(states)
    return states, qtable, reward_matrix