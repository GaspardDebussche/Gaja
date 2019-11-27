# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:11:19 2019

@author: 33766
"""

import numpy as np
import random
from tqdm import tqdm
from time import time

def convert(s):
  try:
    return float(s)
  except ValueError:
    num, denom = s.split('/')
    return float(num) / float(denom)

filename = 'drive/My Drive/CIR/Course exercices/transition_matrix.txt' 
transition_matrix = []

with open(filename, 'r') as f:
  content = f.readlines()

for line in content:
  transition_matrix.append([convert(el) for el in line.split(',')])


filename = 'drive/My Drive/CIR/Course exercices/reward_matrix.txt'
reward_matrix = []

with open(filename, 'r') as f:
  content = f.readlines()

for line in content:
  reward_matrix.append([convert(el) for el in line.split(',')])
  
transition_matrix = np.array(transition_matrix)
reward_matrix = np.array(reward_matrix)
print(transition_matrix)
print(reward_matrix)
state_size, action_size = transition_matrix.shape