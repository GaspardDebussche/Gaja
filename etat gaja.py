# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:30:36 2019

@author: 33766
"""

#Gaja's states
#0,1,2,3,4,5,6
#N,p,eb,er,sp,si,sn
#Neurtral, give the paw, blue eyes, red eyes, positive sound, interrogative sound, negative sound

#Labelisation of Gaja's states
#None,-2,-1,0,1
#Impossible,not interesting,negative,interrogative,positive

import pandas as pd

dataset = pd.read_csv("./data/labelized_gaja_states.csv")

print(dataset.head())