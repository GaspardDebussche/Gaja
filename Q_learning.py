# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:11:19 2019

@author: 33766
"""

######################### GAJA's cat ############################


print(transition_matrix)
print(reward_matrix)
######################### Constants #############################

state_size, action_size = transition_matrix.shape

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

print("Training time is ", time() - start_training)

print(count_1, count_2, qtable)

######################## Reward system ############################

rewards = []

for episode in range(total_test_episodes):
    state = random.randint(0, state_size-1)
    total_rewards = 0

    for step in range(max_steps):

        action = np.argmax(qtable[state,:])
        
        new_state = action
        reward = reward_matrix[state, action]
        
        total_rewards += reward
        
        if new_state == 0:
            rewards.append(total_rewards)
            break
        state = new_state

print('Average score is ', sum(rewards)/total_test_episodes)
print('Maximum score is ', max(rewards))
